from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True) # Email ထည့်မယ်
    hashed_password = Column(String)                # Password ကို Hash လုပ်သိမ်းမယ်
    
    coins = Column(Integer, default=0)
    videos = relationship("Video", back_populates="owner")

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    video_url = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="videos")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    
    # ဒီနေရာမှာ DateTime (SQLAlchemy) ကို သုံးပြီး default ကို datetime.utcnow နဲ့ တွဲပါ
    timestamp = Column(DateTime, default=datetime.utcnow)