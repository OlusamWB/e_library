import pytest
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

new_book = {
    "title": "Test Book",
    "author": "Author Name",
    "is_available": "bool = True"

}

updated_book = {
    "title": "Updated Test Book",
    "author": "Updated Author",
    "is_available": "bool = Talse"    
}

def test_add_book():
    response = client.post("/books", json=new_book)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["title"] == new_book["title"]

def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_book():
    response = client.put("/books/1", json=updated_book)
    assert response.status_code == 200
    assert response.json()["title"] == updated_book["title"]

def test_get_book_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == new_book["title"]

def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted successfully."}
