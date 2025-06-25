from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.schemas.user import UserCreate, UserLogin
from app.crud.user import register_user, authenticate_user

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