from sqlalchemy.orm import Session
from app.models.user import User
from app.models.post import Post
from fastapi import APIRouter, Depends, status, HTTPException
from app.database import get_db
from app.schemas.user import UserUpdate, FollowRequest
from app.schemas.post import PostCreate, PostResponse


def get_profile(username:str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return {"error": "user not found"}
    
    posts = db.query(Post).filter(Post.user_id == user.id).all()
    followers_count = len(user.followers)
    following_count = len(user.following)
    is_following = username in user.followers

    return{
        "username": user.username,
        "bio": user.bio,
        "profile_pic": user.profile_pic,
        "posts": [
            {"id": p.id, 
            "content": p.content, 
            "image_url": p.image_url, 
            "created_at": p.created_at} 
            for p in posts],
        "followers": followers_count,
        "following": following_count,
        "is_following": is_following
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

def create_post(username:str, post_data: PostCreate, db:Session):
    user = db.query(User).filter(User.username==username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not post_data.content and not post_data.image_url:
        raise HTTPException(status_code=400, detail="Post must have content or an image.")
    
    new_post = Post(
        content = post_data.content or "",
        image_url = post_data.image_url,
        user_id = user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {"message":"post added"}

def follow(username:str, otherUser: FollowRequest, db:Session):
    userToFollow = db.query(User).filter(User.username == otherUser.otherUser).first()
    username = db.query(User).filter(User.username == username).first()
    if not userToFollow:
        raise HTTPException(status_code=404, detail="User not found")

    if username == userToFollow:
        raise HTTPException(status_code=400, detail="Cannot follow yourself")
    
    if username in userToFollow.followers:
        userToFollow.followers.remove(username)
        db.commit()
        return {"message": "Unfollowed"}
    else:
        userToFollow.followers.append(username)
        db.commit()
        return {"message": "Followed"}