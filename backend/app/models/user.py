from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
     #index to find results faster and unique so no two accounts have same username
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    bio = Column(String, default = "Hi!")
    profile_pic = Column(String, default = "/images/defaultPFP.jpg")

    #bidirectional relationship between user and posts
    posts = relationship("Post", back_populates="user", cascade="all, delete")