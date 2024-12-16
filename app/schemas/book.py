from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel):
    title: str
    author: str
    is_available: bool = True

class BorrowRecord():
    user_id:str
    book_id: str
    borrow_date: datetime
    return_date: datetime