from typing import List
from typing import Union

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

#トレンド検索
from pytrends.request import TrendReq
import random

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


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/search")
def search_trend():
   pytrend_request = TrendReq(hl="ja-jp", tz=540)
#    words = ["アニメ","映画","旅行","カフェ","アーティスト","PS4", "暇つぶし"]
   words = ["映画", "カフェ", "アニメ"]
   word =  random.choice(words)
   # キーワード一覧
   keywords = [word]
   # 検索範囲の日付
   start_date, end_date = "2023-2-16T00", "2023-2-23T00"
   # 検索リクエストのビルド
   pytrend_request.build_payload(kw_list=keywords, timeframe=f"{start_date} {end_date}", geo="JP")
   # 指定したキーワードの関連キーワード情報を取得する
   related_keywords_info = pytrend_request.related_queries()
   # に関連するトップキーワードの情報を取得する
   related_top_keywords_table = related_keywords_info[word]["rising"]
   print("検索ワード"+str(keywords))
   print("検索結果は")
#    print(related_top_keywords_table.values)
   random_trend = random.choice(related_top_keywords_table.values)
   print(random_trend[0])
   print("トップトレンドは")
   print(related_top_keywords_table.values[0][0])
   print("↓がgoogle検索url")
   print("https://www.google.com/search?q="+related_top_keywords_table.values[0][0]+"&rlz=1C1FQRR_jaJP938JP938&oq="+related_top_keywords_table.values[0][0]+"&aqs=chrome..69i57j0i4i131i433i512j0i67i131i433j0i4i131i433i512j0i67l2j0i131i433i512l2j0i4i131i433i512j0i67.748j0j15&sourceid=chrome&ie=UTF-8")
   return   {"keywords":related_top_keywords_table.values,
            # "trendtop":related_top_keywords_table.values[0][0],
            "trendtop":random_trend[0],
            "googleurl":"https://www.google.com/search?q="+random_trend[0]+"&rlz=1C1FQRR_jaJP938JP938&oq="+random_trend[0]+"&aqs=chrome..69i57j0i4i131i433i512j0i67i131i433j0i4i131i433i512j0i67l2j0i131i433i512l2j0i4i131i433i512j0i67.748j0j15&sourceid=chrome&ie=UTF-8"
            }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


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
