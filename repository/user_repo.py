from sqlalchemy.orm import Session
import models, schemas
from hash import Hash
from fastapi import HTTPException

def create_user(request: schemas.UserCreate, db: Session):
    # User ရှိမရှိ စစ်ခြင်း
    db_user = db.query(models.User).filter(models.User.email == request.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Password Hash လုပ်ခြင်း
    hashed_pwd = Hash.bcrypt(request.password)
    
    new_user = models.User(
        username=request.username, 
        email=request.email, 
        hashed_password=hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user