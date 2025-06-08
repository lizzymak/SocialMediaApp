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