from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import schemas
from database import get_db
from repository import user_repo

router = APIRouter(prefix="/users", tags=["User"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Repository ကို db ပါ တစ်ခါတည်း ပို့ပေးလိုက်ပါ
    return user_repo.create_user(user, db)