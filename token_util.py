from datetime import datetime, timedelta
from jose import JWTError , jwt 
import schemas

SECRET_KEY = 'ab274b5c648e130c4ec09ebb7f8268dd10260d4f35d2ed2a39656cd0fb784cef'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

def create_access_token(data: dict):
    to_encode = data.copy()
    # datetime.utcnow() သည် warning တက်နိုင်၍ timezone.utc ကို သုံးပါ
    from datetime import datetime, timezone
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token : str , credentials_exception ):
    try : 
        payload = jwt.decode(token , SECRET_KEY , algorithms = [ALGORITHM])
        email : str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)

    except JWTError:
        raise credentials_exception