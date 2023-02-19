from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request
from pydantic import BaseModel
from database import User, engine

# DB接続用のセッションクラス インスタンスが作成されると接続する
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pydanticを用いたAPIに渡されるデータの定義 ValidationやDocumentationの機能が追加される
class UserIn(BaseModel):
    email: str
    password: bool

# 単一のUserを取得するためのユーティリティ
def get_user(database_session: Session, user_id: int):
    return database_session.query(User).filter(User.id == user_id).first()

# DB接続のセッションを各エンドポイントの関数に渡す
def get_database(request: Request):
    return request.state.database

# このインスタンスをアノテーションに利用することでエンドポイントを定義できる
app = FastAPI()

# Userの全取得
@app.get("/users/")
def read_users(database: Session = Depends(get_database)):
    users = database.query(User).all()
    return users

# 単一のUserを取得
@app.get("/users/{user_id}")
def read_user(user_id: int, database: Session = Depends(get_database)):
    user = get_user(database, user_id)
    return user

# Userを登録
@app.post("/users/")
async def create_user(user_in: UserIn,  database: Session = Depends(get_database)):
    user = User(email=user_in.email, password=False)
    database.add(user)
    database.commit()
    user = get_user(database, user.id)
    return user

# Userを更新
@app.put("/users/{user_id}")
async def update_user(user_id: int, user_in: UserIn, database: Session = Depends(get_database)):
    user = get_user(database, user_id)
    user.email = user_in.email
    user.password = user_in.password
    database.commit()
    user = get_user(database, user_id)
    return user

# Userを削除
@app.delete("/users/{user_id}")
async def delete_user(user_id: int, database: Session = Depends(get_database)):
    user = get_user(database, user_id)
    database.delete(user)
    database.commit()

# リクエストの度に呼ばれるミドルウェア DB接続用のセッションインスタンスを作成
@app.middleware("http")
async def database_session_middleware(request: Request, call_next):
    request.state.database = SessionLocal()
    response = await call_next(request)
    request.state.database.close()
    return response