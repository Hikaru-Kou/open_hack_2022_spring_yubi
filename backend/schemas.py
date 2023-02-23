from typing import List, Optional

from pydantic import BaseModel

class GenreBase(BaseModel):
    Genre: str
    

class Genre(GenreBase):
    id: int

    class Config:
       orm_mode = True

class GenreCreate(GenreBase):
   pass

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
   password: str

class User(UserBase):
   id: int
   is_free: bool

   class Config:
       orm_mode = True