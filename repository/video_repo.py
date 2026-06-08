from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException

def create_video(video: schemas.VideoCreate, user_id: int, db: Session):
    # User ရှိမရှိ စစ်ဆေးခြင်း
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Video အသစ်ဖန်တီးခြင်း
    new_video = models.Video(
        title=video.title, 
        video_url=video.video_url, 
        owner_id=user_id
    )
    db.add(new_video)
    db.commit()
    db.refresh(new_video)
    return new_video

def get_all_videos(db: Session):
    return db.query(models.Video).all()