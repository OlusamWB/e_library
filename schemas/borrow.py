from pydantic import BaseModel
from datetime import datetime

class BorrowBase(BaseModel):
    user_id: str
    book_id: str
    borrow_date: datetime = datetime.now()
    return_date: datetime | None = None

class Borrow_Book(BorrowBase):
    id: str

class BorrowReturned(BorrowBase):
    pass