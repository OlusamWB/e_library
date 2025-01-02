from fastapi import APIRouter, HTTPException
from typing import List
from schemas.user import UserCreate, UserUpdate, UserResponse
from services.user import UserCrud

user_router = APIRouter()

# Get all users
@user_router.get("/users", response_model=List[UserResponse])
def get_all_users():
    try:
        return UserCrud.get_users()
    except Exception:
        raise HTTPException(status_code=500, detail="Could not retrieve users.")

@user_router.get("/users/", response_model=UserResponse)
def get_user(email: str):
    try:
        user = UserCrud.get_user_by_email(email)
        if user:
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create a new user
@user_router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    try:
        return UserCrud.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not create user: {str(e)}")

# Update user details
@user_router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    try:
        return UserCrud.update_user(user_id, user)
    except Exception:
        raise HTTPException(status_code=400, detail="Could not update user.")

# Delete a user
@user_router.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        UserCrud.delete_user(user_id)
        return {"message": "User deleted successfully."}
    except Exception:
        raise HTTPException(status_code=400, detail="Could not delete user.")

# Deactivate a user
@user_router.patch("/users/{user_id}/deactivate")
def deactivate_user(user_id: int):
    try:
        UserCrud.deactivate_user(user_id)
        return {"message": "User deactivated successfully."}
    except Exception:
        raise HTTPException(status_code=400, detail="Could not deactivate user.")
