from fastapi import APIRouter, HTTPException
from typing import List
from schemas.book import BookCreate, BookUpdate, BookResponse
from services.book import BookCrud

book_router = APIRouter()

# Get all books
@book_router.get("/books", response_model=List[BookResponse])
def get_all_books():
    return BookCrud.get_all_books()

# Get a specific book by ID
@book_router.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    book = BookCrud.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book

# Create a new book
@book_router.post("/books", response_model=BookResponse)
def create_book(book: BookCreate):
    return BookCrud.create_book(book)

# Update book details
@book_router.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate):
    updated_book = BookCrud.update_book(book_id, book)
    if not updated_book:
        raise HTTPException(status_code=400, detail="Could not update book.")
    return updated_book

# Delete a book
@book_router.delete("/books/{book_id}")
def delete_book(book_id: int):
    success = BookCrud.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=400, detail="Could not delete book.")
    return {"message": "Book deleted successfully."}

# Mark a book as unavailable
@book_router.patch("/books/{book_id}/unavailable")
def mark_book_unavailable(book_id: int):
    success = BookCrud.mark_book_unavailable(book_id)
    if not success:
        raise HTTPException(status_code=400, detail="Could not mark book as unavailable.")
    return {"message": "Book marked as unavailable."}

# Borrow a book
# @book_router.post("/borrow-book/")
# def borrow_book(request: BorrowRequest):
#     message = BookCrud.borrow_book(request.book_id, request.borrower_name)
#     if not message:
#         raise HTTPException(status_code=400, detail="Could not borrow book.")
#     return {"message": message}

# Return a book
# @book_router.post("/return-book/")
# def return_book(request: ReturnRequest):
#     message = BookCrud.return_book(request.book_id)
#     if not message:
#         raise HTTPException(status_code=400, detail="Could not return book.")
#     return {"message": message}