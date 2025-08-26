from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from backend.app.database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    #establish relationship  to User model
    user = relationship("User", back_populates="posts")