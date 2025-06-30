"""CRUD"""
from typing import Optional
from sqlalchemy.orm import Session
from schemas import UserCreate

from shared.models import User
from shared.auth import get_password_hash


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """get user"""
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate) -> User:
    """create user"""
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
