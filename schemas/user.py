from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool = True

class Login(UserBase):
    email: str
    password: str

class UserCreate(UserBase):
    pass

class UserStatus(UserBase):
    is_active: bool = False
