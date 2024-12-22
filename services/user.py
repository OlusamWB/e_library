from fastapi import HTTPException
from schemas.user import UserBase, UserCreate, UserOut, UserUpdate
from passlib.context import CryptContext  # For password hashing

# In-memory list of users (you may want to switch this to a real database later)
users = [
    UserBase(id=1, name="Olumide", email="olumighty@gmail.com", password="1234", is_active=True),
    UserBase(id=2, name="Samuel", email="Samguy@gmail.com", password="5678", is_active=True),
    UserBase(id=3, name="Ayomide", email="Ayhigh@gmail.com", password="1011", is_active=True),
]

# Initialize the password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCrud:
    @staticmethod
    def get_users():
        return [UserOut(id=user.id, name=user.name, email=user.email, is_active=user.is_active) for user in users]

    @staticmethod
    def get_user_by_email(email: str):
        for user in users:
            if user.email == email:
                return UserOut(id=user.id, name=user.name, email=user.email, is_active=user.is_active)
        raise HTTPException(status_code=404, detail="User not found")
    
    @staticmethod
    def create_user(user_create: UserCreate) -> UserOut:
        # Check if the email already exists
        for user in users:
            if user.email == user_create.email:
                raise HTTPException(status_code=400, detail="Email already in use")
        
        # Hash the password before saving it
        hashed_password = pwd_context.hash(user_create.password)
        
        # Create the user and add to the list
        new_user = UserBase(
            id=len(users) + 1,  # Simple ID generation
            name=user_create.name,
            email=user_create.email,
            password=hashed_password,
            is_active=user_create.is_active
        )
        users.append(new_user)
        return UserOut(id=new_user.id, name=new_user.name, email=new_user.email, is_active=new_user.is_active)

    @staticmethod
    def update_user(user_id: int, user_update: UserUpdate) -> UserOut:
        for user in users:
            if user.id == user_id:
                # Update fields if provided
                user.name = user_update.name if user_update.name else user.name
                user.email = user_update.email if user_update.email else user.email
                if user_update.password:
                    user.password = pwd_context.hash(user_update.password)  # Hash the new password
                user.is_active = user_update.is_active if user_update.is_active is not None else user.is_active
                return UserOut(id=user.id, name=user.name, email=user.email, is_active=user.is_active)
        raise HTTPException(status_code=404, detail="User not found")
