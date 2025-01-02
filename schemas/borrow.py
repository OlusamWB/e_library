from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
# Base schema for borrow records (user and book identifiers)
class BorrowRecordBase(BaseModel):
    user_id: int
    book_id: int

class BorrowCreate(BorrowRecordBase):
    borrow_date: date

class BorrowRecordResponse(BorrowRecordBase):
    id: int
    borrow_date: datetime
    return_date: Optional[datetime] = None

class BorrowReturn(BaseModel):
    return_date: date

class BorrowOut(BorrowRecordBase):
    id: int
    borrow_date: date
    return_date: Optional[date] = None  

    class Config:
        orm_mode = True  

class BorrowRequest(BaseModel):
    book_id: int
    user_id: int
    borrower_name: str

class ReturnRequest(BaseModel):
    book_id: int
    user_id: int
    borrower_name: str
