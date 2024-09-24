from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse,UserUpdate
from crud.user import create_user, get_user,update_user
from db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    return db_user

@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=UserUpdate)
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user