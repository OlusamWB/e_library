from fastapi import APIRouter
from service.book import BookCrud

book_router = APIRouter()

@book_router.get("/books")
def get_all_books():
    return BookCrud.get_all_books()
