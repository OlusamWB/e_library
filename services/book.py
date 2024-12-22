from schemas.book import BookCreate, BookUpdate, BookResponse
from typing import List

# Mock database
books = [
    BookResponse(id=1, title="Clean Code", author="Robert C. Martin", is_available=True),
    BookResponse(id=2, title="The Pragmatic Programmer", author="Andrew Hunt", is_available=True),
    BookResponse(id=3, title="Introduction to Algorithms", author="Thomas H. Cormen", is_available=False),
]

class BookCrud:
    @staticmethod
    def get_all_books() -> List[BookResponse]:
        return books

    @staticmethod
    def get_book_by_id(book_id: int) -> BookResponse:
        for book in books:
            if book.id == book_id:
                return book
        return None

    @staticmethod
    def create_book(new_book: BookCreate) -> BookResponse:
        new_id = max(book.id for book in books) + 1 if books else 1
        created_book = BookResponse(
            id=new_id,
            title=new_book.title,
            author=new_book.author,
            is_available=new_book.is_available,
        )
        books.append(created_book)
        return created_book

    @staticmethod
    def update_book(book_id: int, updated_book: BookUpdate) -> BookResponse:
        book = BookCrud.get_book_by_id(book_id)
        if not book:
            return None
        book.title = updated_book.title
        book.author = updated_book.author
        book.is_available = updated_book.is_available
        return book

    @staticmethod
    def delete_book(book_id: int) -> bool:
        global books
        books = [book for book in books if book.id != book_id]
        return True

    @staticmethod
    def mark_book_unavailable(book_id: int) -> bool:
        book = BookCrud.get_book_by_id(book_id)
        if book:
            book.is_available = False
            return True
        return False

    @staticmethod
    def borrow_book(book_id: int, borrower_name: str) -> str:
        book = BookCrud.get_book_by_id(book_id)
        if book and book.is_available:
            book.is_available = False
            return f"Book '{book.title}' has been borrowed by {borrower_name}."
        return None

    @staticmethod
    def return_book(book_id: int) -> str:
        book = BookCrud.get_book_by_id(book_id)
        if book and not book.is_available:
            book.is_available = True
            return f"Book '{book.title}' has been returned."
        return None
