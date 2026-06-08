from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    coins: int
    
    class Config:
        from_attributes = True

class VideoCreate(BaseModel):
    title: str
    video_url: str

class Video(VideoCreate):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class Message(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True


class Login(BaseModel):
    email: EmailStr
    password: str

class TokenData(BaseModel):
    email: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str