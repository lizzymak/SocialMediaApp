from pydantic import BaseModel, EmailStr

#expected feilds when creating a user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

#expected feilds when logging in a user
class UserLogin(BaseModel):
    username: str
    password: str

#expected fields when updating profile
class UserUpdate(BaseModel):
    username: str | None = None  #if user doesnt change this its set to None
    bio: str | None = None
    profile_pic: str | None = None

class FollowRequest(BaseModel): #class for following a user
    otherUser: str