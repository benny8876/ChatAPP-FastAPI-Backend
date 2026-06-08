from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
from database import get_db
from oauth2 import oauth2_scheme
from repository import video_repo

router = APIRouter(prefix="/videos", tags=["Videos"])

@router.post("/", response_model=schemas.Video)
def create_video(video: schemas.VideoCreate, user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    # Repository ကို လိုအပ်တဲ့ data များ ပို့ပေးခြင်း
    return video_repo.create_video(video, user_id, db)

@router.get("/", response_model=list[schemas.Video])
def get_videos(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return video_repo.get_all_videos(db)