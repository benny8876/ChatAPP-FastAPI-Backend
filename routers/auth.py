from fastapi import APIRouter,  status, Depends ,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models ,token_util
from hash import Hash 
from database import get_db



router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 1. User ရှိမရှိ စစ်မယ်
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    # 2. Password စစ်မယ်
    if not Hash.verify(request.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    # 3. [အရေးကြီး] Token ထုတ်ပေးခြင်း
    access_token = token_util.create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}