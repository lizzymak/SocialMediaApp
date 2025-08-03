from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.schemas.user import UserCreate, UserLogin
from app.crud.user import register_user, authenticate_user
from app.crud.profile import get_profile as get_profile_data
from app.crud.profile import update_profile as update_profile_data
from app.schemas.user import UserUpdate

app = FastAPI()

origins =[
    "http://localhost:3000",
    "http://127.0.0.1:3000"
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