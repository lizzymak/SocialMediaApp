from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostCreate(BaseModel): #createpost
    content: Optional[str]
    image_url: Optional[str] = None

class PostResponse(PostCreate): #return post details
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # allows conversion from SQLAlchemy models

