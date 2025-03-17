from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CallReportBase(BaseModel):
    userId: str
    phoneNumber: str
    timestamp: str

class CallReportCreate(CallReportBase):
    pass

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class ReportedCallResponse(BaseModel):
    id: int
    userId: str = Field(alias="user_id")  # Map to SQLAlchemy's user_id
    phoneNumber: str = Field(alias="phone_number")  # Map to SQLAlchemy's phone_number
    timestamp: datetime
    
    model_config = ConfigDict(
        from_attributes=True,  # Allows ORM model loading
        populate_by_name=True  # Enable both field names and aliases
    )