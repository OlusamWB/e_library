# import pytest
# from fastapi.testclient import TestClient
# from main import app  # Import your FastAPI app

# client = TestClient(app)

# # Test data
# borrow_request = {
#     "book_id": 1,
#     "borrower_name": "John Doe"
# }

# return_request = {
#     "book_id": 1,
#     "user_id": 1
# }

# # Test: Borrow a book
# def test_borrow_book():
#     response = client.post("/borrow-book/", json=borrow_request)
#     assert response.status_code == 200
#     assert response.json() == {"message": "Book borrowed successfully."}

# # Get all borrow records
# def test_get_all_borrow_records():
#     response = client.get("/borrow-records")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# # Get borrow records for a specific user
# def test_get_user_borrow_records():
#     response = client.get("/borrow-records/1")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# #Return a book
# def test_return_book():
#     response = client.post("/return-book/", json=return_request)
#     assert response.status_code == 200
#     assert response.json() == {"message": "Book returned successfully."}

# # Borrowing with invalid book_id
# def test_borrow_book_invalid_book_id():
#     invalid_borrow_request = {
#         "book_id": 999,  # Assuming book 999 doesn't exist
#         "borrower_name": "John Doe"
#     }
#     response = client.post("/borrow-book/", json=invalid_borrow_request)
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Book not available."}

# # Returning a book with incorrect user_id
# def test_return_book_invalid_user():
#     invalid_return_request = {
#         "book_id": 1,
#         "user_id": 999  # Assuming user 999 doesn't exist
#     }
#     response = client.post("/return-book/", json=invalid_return_request)
#     assert response.status_code == 400
#     assert response.json() == {"detail": "User record not found."}
