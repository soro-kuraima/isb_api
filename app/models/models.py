from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    reported_calls = relationship("ReportedCall", back_populates="user")
    
class ReportedCall(Base):
    __tablename__ = "reported_calls"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    phone_number = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    
    # Relationship
    user = relationship("User", back_populates="reported_calls")