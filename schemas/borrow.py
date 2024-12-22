from pydantic import BaseModel
from datetime import date
from typing import Optional

# Base schema for borrow records (user and book identifiers)
class BorrowRecordBase(BaseModel):
    user_id: int
    book_id: int

# Schema for creating a borrow record (borrow_date is required)
class BorrowCreate(BorrowRecordBase):
    borrow_date: date

# Schema for the return operation (requires return_date)
class BorrowReturn(BaseModel):
    return_date: date

# Schema for the borrowed record with optional return_date
class BorrowOut(BorrowRecordBase):
    id: int
    borrow_date: date
    return_date: Optional[date] = None  # Marked optional because the book may not be returned yet

    class Config:
        orm_mode = True  # If using ORM like SQLAlchemy, this is needed for compatibility

# Alternative names for request models to be used in routes (e.g., BorrowRequest, ReturnRequest)
class BorrowRequest(BaseModel):
    book_id: int
    borrower_name: str

class ReturnRequest(BaseModel):
    book_id: int