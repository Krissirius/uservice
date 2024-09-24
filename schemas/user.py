from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    login: str
    userName: str
    email: EmailStr
    numberPhone: str

class UserCreate(UserBase):
    password: str # При создании пользователя принимаем обычный пароль
    
    
class UserInDB(UserBase):
    id: int
    status: bool

    class Config:
        from_attributes = True

class UserResponse(UserBase):
    id: int
    status: bool
    idDepartment: Optional[int]
    idElecSignature:Optional[int]
    code: Optional[str]
    accept: bool
    share: bool
    created: bool
    checked: bool
    closed: bool
    contract: bool
    admin: bool
    editor: bool
    completed: bool
    techSpecification: bool

    # Updated configuration for Pydantic v2
    class Config:
        from_attributes = True  # Use this instead of orm_mode in Pydantic v2

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]    
    status: Optional[bool]
    idDepartment: Optional[int]
    idElecSignature:Optional[int]
    code: Optional[str]
    accept: Optional[bool]
    share: Optional[bool]
    created: Optional[bool]
    checked: Optional[bool]
    closed: Optional[bool]
    contract: Optional[bool]
    admin: Optional[bool]
    editor: Optional[bool]
    completed: Optional[bool]
    techSpecification: Optional[bool]

    class Config:
        from_attributes = True