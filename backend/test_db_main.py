from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import crud
import models
import schemas
from database import SessionLocal, engine

# テーブルの作成
models.Base.metadata.create_all(bind=engine)


app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB接続セッション作成
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


@app.get("/test")
def test_response():
   return {'message': 'test'}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
   db_user = crud.get_user_by_email(db, email=user.email)
   if db_user:
       raise HTTPException(status_code=400, detail="Email already registered")
   return crud.create_user(db=db, user=user)


@app.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
   users = crud.get_users(db, skip=skip, limit=limit)
   return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
   db_user = crud.get_user(db, user_id=user_id)
   if db_user is None:
       raise HTTPException(status_code=404, detail="User not found")
   return db_user

@app.get("/genres/", response_model=List[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
   genres = crud.get_genres(db, skip=skip, limit=limit)
   return genres