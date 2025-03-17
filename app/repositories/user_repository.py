from sqlalchemy.orm import Session
from typing import Optional, List
from ..models.models import User
from ..schemas.user import UserCreate, UserResponse

class UserRepository:
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        db_user = User(
            id=user.id,
            name=user.name,
            location=user.location
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: str) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()