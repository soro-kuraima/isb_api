from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from ..models.models import ReportedCall
from ..schemas.call import CallReportCreate

class CallRepository:
    @staticmethod
    def create_call_report(db: Session, call_report: CallReportCreate) -> ReportedCall:
        try:
            timestamp = datetime.fromisoformat(call_report.timestamp)
        except ValueError:
            timestamp = datetime.utcnow()
            
        db_call = ReportedCall(
            user_id=call_report.userId,
            phone_number=call_report.phoneNumber,
            timestamp=timestamp
        )
        db.add(db_call)
        db.commit()
        db.refresh(db_call)
        return db_call
    
    @staticmethod
    def get_calls_by_user_id(db: Session, user_id: str) -> List[ReportedCall]:
        return db.query(ReportedCall).filter(
            ReportedCall.user_id == user_id
        ).order_by(ReportedCall.timestamp.desc()).all()
    
    @staticmethod
    def get_call_by_id(db: Session, call_id: int) -> Optional[ReportedCall]:
        return db.query(ReportedCall).filter(ReportedCall.id == call_id).first()