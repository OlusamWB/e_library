from fastapi import APIRouter
from services.user import UserCrud

user_router = APIRouter()

@user_router.get("/users")
def get_all_users():
    return UserCrud.get_users()

@user_router.get("/users/")
def get_user(email: str):
    return UserCrud.get_user_by_email(email)




# @user.router.post("/users", status_code=status.HTTP_201_CREATED)
# def create_user(user: UserBase):
#     return UserCrud.create_user(user)