from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BorrowRequest(BaseModel):
    book_id: int
    borrower_name: str

class ReturnRequest(BaseModel):
    book_id: int

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
