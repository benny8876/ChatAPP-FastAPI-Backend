from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./music_app.db"

# Database Engine ကို ဖန်တီးခြင်း
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Database Session ကို ဖန်တီးခြင်း (ဒါက API တွေထဲမှာ သုံးဖို့ပါ)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database Model တွေ အားလုံးရဲ့ အခြေခံ (Base)
Base = declarative_base()

# Database ချိတ်ဆက်မှုကို ရယူရန်အတွက် Function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()