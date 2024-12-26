from datetime import datetime
from typing import List
from schemas.borrow import BorrowRecordResponse

# Mock database for borrow records and books
borrow_records = []
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "is_available": True},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "is_available": True},
]

class BorrowCrud:
    @staticmethod
    def get_all_borrow_records() -> List[BorrowRecordResponse]:
        """Retrieve all borrow records."""
        return borrow_records

    @staticmethod
    def get_borrow_records_by_user(user_id: int) -> List[BorrowRecordResponse]:
        """Retrieve borrow records for a specific user."""
        user_records = [
            record for record in borrow_records if record["user_id"] == user_id
        ]
        return user_records

    @staticmethod
    def borrow_book(book_id: int, user_id: int) -> str:
        """Borrow a book if available."""
        # Check if book exists and is available
        book = next((book for book in books if book["id"] == book_id), None)
        if not book:
            raise ValueError("Book not found.")
        if not book["is_available"]:
            raise ValueError("Book is not available for borrowing.")

        # Create a new borrow record
        borrow_record = {
            "id": len(borrow_records) + 1,
            "user_id": user_id,
            "book_id": book_id,
            "borrow_date": datetime.now(),
            "return_date": None,
        }
        borrow_records.append(borrow_record)

        # Mark the book as unavailable
        book["is_available"] = False
        return f"Book '{book['title']}' has been borrowed successfully."

    @staticmethod
    def return_book(book_id: int, user_id: int) -> str:
        """Return a borrowed book."""
        # Find the borrow record
        record = next(
            (record for record in borrow_records if record["book_id"] == book_id and record["user_id"] == user_id),
            None,
        )
        if not record:
            raise ValueError("No matching borrow record found.")
        if record["return_date"]:
            raise ValueError("Book has already been returned.")

        # Update the return date in the borrow record
        record["return_date"] = datetime.now()

        # Mark the book as available
        book = next((book for book in books if book["id"] == book_id), None)
        if book:
            book["is_available"] = True

        return f"Book '{book['title']}' has been returned successfully."
