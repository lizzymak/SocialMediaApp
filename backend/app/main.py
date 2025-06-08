from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal

app = FastAPI()

@app.get("/testdb")
def test_db():
    return {"message": "Connected to db!!"}