from pydantic import BaseModel

# Base schema for Book
class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True

# Schema for creating a new book
class BookCreate(BookBase):
    pass

# Schema for updating an existing book
class BookUpdate(BookBase):
    pass

# Schema for book response
class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True

# Schema for borrowing a book
class BorrowRequest(BaseModel):
    book_id: int
    borrower_name: str

# Schema for returning a book
class ReturnRequest(BaseModel):
    book_id: int