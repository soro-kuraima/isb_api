from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..repositories.user_repository import UserRepository
from ..schemas.user import UserCreate, UserResponse

class UserService:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> UserResponse:
        # Check if user already exists
        db_user = UserRepository.get_user_by_id(db, user_data.id)
        if db_user:
            raise HTTPException(status_code=400, detail="User ID already registered")
        
        # Create new user
        user = UserRepository.create_user(db, user_data)
        return UserResponse.from_orm(user)
    
    @staticmethod
    def get_user(db: Session, user_id: str) -> UserResponse:
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse.from_orm(user)