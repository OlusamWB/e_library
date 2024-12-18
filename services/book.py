from schemas.book import Book, BorrowRecord

books = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", publication_year=2008, is_available=True),
    Book(id=2, title="The Pragmatic Programmer", author="Andrew Hunt", publication_year=1999, is_available=True),
    Book(id=3, title="Introduction to Algorithms", author="Thomas H. Cormen", publication_year=2009, is_available=False),
]

class BookCrud:
    @staticmethod
    def get_all_books():
        return books
    
