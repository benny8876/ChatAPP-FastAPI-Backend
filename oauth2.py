from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
import token_util # မင်းရဲ့ token_utils ကို import လုပ်ပါ

# login endpoint ကို tokenUrl အဖြစ် သတ်မှတ်ပေးပါ
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # verify_token ကို ခေါ်ပြီး user email ကို ပြန်ယူမယ်
    return token_util.verify_token(token, credentials_exception)