from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
#from core.security import hash_password
import bcrypt
from schemas.user import UserUpdate
from typing import Optional

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_login(db: Session, login: str):
    return db.query(User).filter(User.login == login).first()

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)  # Хешируем пароль
    db_user = User(
        login=user.login, 
        userName=user.userName,
        email=user.email,
        numberPhone=user.numberPhone,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    # Обновляем поля, которые были переданы
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user