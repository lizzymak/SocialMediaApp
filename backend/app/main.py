from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal, get_db
from backend.app.schemas.user import UserCreate, UserLogin, UserUpdate, FollowRequest
from backend.app.crud.user import register_user, authenticate_user
from backend.app.crud.profile import get_profile as get_profile_data
from backend.app.crud.profile import update_profile as update_profile_data
from backend.app.crud.profile import create_post as create_post_data
from backend.app.crud.profile import follow as follow_user
from backend.app.crud.profile import feed as get_feed
from backend.app.schemas.post import PostCreate

app = FastAPI()

origins =[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://socialmediaapp-nzgu.onrender.com",
    "https://social-media-app-lizzymaks-projects.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.get("/testdb")
def test_db():
    return {"message": "Connected to db!!"}

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user.username, user.email, user.password)

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(db, user.username, user.password)

@app.get("/profile/{username}")
def get_profile(username:str, db: Session = Depends(get_db)):
    return get_profile_data(username, db)

@app.patch("/profile/{username}")
def update_profile(update_data: UserUpdate, username:str, db: Session = Depends(get_db)):
    return update_profile_data(update_data, username, db)

@app.post("/profile/post/{username}")
def create_post(username:str, post_data: PostCreate, db: Session = Depends(get_db)):
    return create_post_data(username, post_data, db)

@app.post("/profile/follow/{username}")
def follow(username: str, otherUser: FollowRequest, db: Session = Depends(get_db)):
    return follow_user(username, otherUser, db)

@app.get("/feed/{username}")
def feed(username: str, db: Session = Depends(get_db)):
    return get_feed(username, db)