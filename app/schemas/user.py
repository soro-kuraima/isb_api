from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    id: str
    name: str
    location: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    created_at: datetime
    
    class Config:
        from_attributes = True