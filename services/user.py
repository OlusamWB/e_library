from fastapi import HTTPException
from schemas.user import UserCreate, UserUpdate, UserResponse
from passlib.context import CryptContext  # For password hashing

# In-memory list of users (dictionary representation)
users = [
    {"id": 1, "name": "Olumide", "email": "olumighty@gmail.com", "password": "1234", "is_active": True},
    {"id": 2, "name": "Samuel", "email": "Samguy@gmail.com", "password": "5678", "is_active": True},
    {"id": 3, "name": "Ayomide", "email": "Ayhigh@gmail.com", "password": "1011", "is_active": True},
]

# Initialize the password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCrud:
    @staticmethod
    def get_users():
        return users

    @staticmethod
    def get_user_by_email(email: str) -> UserResponse:
        for user in users:
            if user["email"] == email:
                return UserResponse(**user)
        raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def create_user(user_create: UserCreate) -> UserResponse:
        # Check if the email already exists
        if any(user["email"] == user_create.email for user in users):
            raise HTTPException(status_code=400, detail="Email already in use")

        # Hash the password before saving it
        hashed_password = pwd_context.hash(user_create.password)

        # Create the user and add to the list
        new_user = {
            "id": len(users) + 1,  # Simple ID generation
            "name": user_create.name,
            "email": user_create.email,
            "password": hashed_password,
            "is_active": user_create.is_active,
        }
        users.append(new_user)
        return UserResponse(**new_user)

    @staticmethod
    def update_user(user_id: int, user_update: UserUpdate) -> UserResponse:
        for user in users:
            if user["id"] == user_id:
                
                if user_update.name:
                    user["name"] = user_update.name
                if user_update.email:
                    user["email"] = user_update.email
                if user_update.password:
                    user["password"] = pwd_context.hash(user_update.password)
                if user_update.is_active is not None:
                    user["is_active"] = user_update.is_active
                return UserResponse(**user)
        raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def delete_user(user_id: int):
        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                return
        raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def deactivate_user(user_id: int):
        for user in users:
            if user["id"] == user_id:
                user["is_active"] = False
                return
        raise HTTPException(status_code=404, detail="User not found")
