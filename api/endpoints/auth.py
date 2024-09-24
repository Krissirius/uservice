from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas.user import UserCreate, UserResponse
from crud.user import create_user, get_user_by_login
from fastapi.security import OAuth2PasswordRequestForm
from core.security import verify_password, create_access_token
from datetime import timedelta

router = APIRouter()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_login(db, login=user.login)
    if existing_user:
        raise HTTPException(status_code=400, detail="Login already registered")
    return create_user(db=db, user=user)

# Эндпоинт для получения токена
@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_login(db, login=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.login}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}