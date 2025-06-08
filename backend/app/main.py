from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.schemas.user import UserCreate, UserLogin
from app.crud.user import register_user, authenticate_user

app = FastAPI()

@app.get("/testdb")
def test_db():
    return {"message": "Connected to db!!"}

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user.username, user.email, user.password)

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(db, user.username, user.password)