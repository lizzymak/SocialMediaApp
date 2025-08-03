from sqlalchemy.orm import Session
from app.models.user import User
from app.models.post import Post
from fastapi import APIRouter, Depends, status, HTTPException
from app.database import get_db
from app.schemas.user import UserUpdate


def get_profile(username:str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return {"error": "user not found"}
    
    posts = db.query(Post).filter(Post.user_id == user.id).all()

    return{
        "username": user.username,
        "bio": user.bio,
        "profile_pic": user.profile_pic,
        "posts": [
            {"id": p.id, 
            "content": p.content, 
            "created_at": p.created_at} 
            for p in posts]
    }

def update_profile(update_data: UserUpdate, username:str, db:Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if update_data.username:
        user.username = update_data.username
    if update_data.profile_pic:
        user.profile_pic = update_data.profile_pic
    if update_data.bio:
        user.bio = update_data.bio

    db.commit()
    db.refresh(user)
    return {"message": "profile updated"}