from fastapi import FastAPI
from routers import auth, user, video, chat

app = FastAPI()

# Router များကို Register လုပ်ခြင်း
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(video.router)
app.include_router(chat.router)

@app.get("/")
def read_root():
    return {"message": "Music Platform Backend is Running!"}

