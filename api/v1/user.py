from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas.user import UserCreate, UserResponse, UsersResponse, UserUpdate
from crud.user import create_user, get_user, get_users, update_user
from db.session import SessionLocal
from core.security import get_current_user  # Импортируем функцию для проверки токена
from models.user import User  # Импорт модели пользователя

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для создания нового пользователя
@router.post("/users/", response_model=UserResponse)
def create_new_user(
    user: UserCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)  # Защищаем JWT
):
    db_user = create_user(db=db, user=user)
    return db_user

# Эндпоинт для получения пользователя по ID
@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)  # Защищаем JWT
):
    db_user = get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Эндпоинт для получения списка пользователей
@router.get("/users/", response_model=List[UsersResponse])
def read_users(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)  # Защищаем JWT
):
    db_user = get_users(db=db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Users not found")
    return db_user

# Эндпоинт для обновления пользователя
@router.put("/users/{user_id}", response_model=UserUpdate)
def update_user_endpoint(
    user_id: int, 
    user: UserUpdate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)  # Защищаем JWT
):
    db_user = update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user