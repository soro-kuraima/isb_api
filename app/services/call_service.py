from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from ..repositories.call_repository import CallRepository
from ..repositories.user_repository import UserRepository
from ..schemas.call import CallReportCreate, ReportedCallResponse

class CallService:
    @staticmethod
    def report_call(db: Session, call_data: CallReportCreate) -> dict:
        # Check if user exists
        user = UserRepository.get_user_by_id(db, call_data.userId)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Create call report
        CallRepository.create_call_report(db, call_data)
        return {"status": "success", "message": "Call reported successfully"}
    
    @staticmethod
    def get_user_calls(db: Session, user_id: str) -> List[ReportedCallResponse]:
        # Check if user exists
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Get call reports
        calls = CallRepository.get_calls_by_user_id(db, user_id)
        return [ReportedCallResponse.model_validate(call) for call in calls]
