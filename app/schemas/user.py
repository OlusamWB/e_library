from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_active: bool = True

class Login(UserBase):
    email: EmailStr
    password: str

class UserStatus(UserBase):
    is_active: bool = False