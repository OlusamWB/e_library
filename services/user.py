from fastapi import Body, status, HTTPException
from schemas.user import UserBase, Login, UserStatus, UserCreate

users = [
    UserBase(id=1, name="Olumide", email="olumighty@gmail.com", password="1234", is_active=True),
    UserBase(id=2, name="Samuel", email="Samguy@gmail.com", password="5678", is_active=True),
    UserBase(id=3, name="Ayomide", email="Ayhigh@gmail.com", password="1011", is_active=True),
]

class UserCrud:
    @staticmethod
    def get_users():
        return users

    @staticmethod
    def get_user_by_email(email: str):
        for user in users:
            if user.email == email:
                return user
        raise HTTPException(status_code=404, detail="User not found")
    
    
