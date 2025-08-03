from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.hash import hash_password, verify_password
from app.auth.jwt import create_access_token
from fastapi import HTTPException, status

def register_user(db: Session, username: str, email: str, password: str):
    #checks if username and email is already registered
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = User(
        username = username,
        email = email,
        hashed_password = hash_password(password)
    )

    #adds user to db
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User registerd"}

def authenticate_user(db: Session, username: str, password: str):
    #searches User table, filters based on condition(when column username has a row that equals def username), rteurn first result
    user = db.query(User).filter(User.username == username).first()
    #checks user exists and that password matches
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    token = create_access_token({"sub": user.username})
    return {"access token": token, "token_type": "bearer", "user_id": user.id, "username": user.username}

