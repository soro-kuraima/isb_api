from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.call import CallReportCreate, ReportedCallResponse
from ..services.call_service import CallService

router = APIRouter(
    prefix="/calls",
    tags=["calls"],
    responses={404: {"description": "Not found"}},
)

@router.post("/report", status_code=status.HTTP_201_CREATED)
def report_call(call: CallReportCreate, db: Session = Depends(get_db)):
    return CallService.report_call(db, call)

@router.get("/user/{user_id}", response_model=List[ReportedCallResponse])
def get_user_calls(user_id: str, db: Session = Depends(get_db)):
    return CallService.get_user_calls(db, user_id)