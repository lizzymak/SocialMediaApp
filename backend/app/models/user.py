from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from backend.app.database import Base

followers_table = Table( #association table
    "followers",
    Base.metadata,
    Column("follower_id", Integer, ForeignKey("users.id", ondelete="CASCADE")), #the user following somebody
    Column("followed_id", Integer, ForeignKey("users.id", ondelete="CASCADE")) #the user being followed
)

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

    followers = relationship(
        "User", #self referential many to many
        secondary=followers_table, #use as bridge table
        primaryjoin=id == followers_table.c.followed_id, #this user is followed by somebody
        secondaryjoin=id == followers_table.c.follower_id, #user is the one doing the following
        backref="following" #creates property .following (represents people this user follows)
    )