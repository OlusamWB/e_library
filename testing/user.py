# import pytest
# from fastapi.testclient import TestClient
# from main import app  # Import your FastAPI app

# client = TestClient(app)

# new_user = {
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "password": "password123",
#     "is_active": True
# }

# updated_user = {
#     "name": "John Updated",
#     "email": "john.updated@example.com",
#     "password": "newpassword123",
#     "is_active": True
# }

# # Create a new user
# def test_create_user():
#     response = client.post("/users", json=new_user)
#     assert response.status_code == 200
#     assert "id" in response.json()
#     assert response.json()["email"] == new_user["email"]

# # Get all users
# def test_get_all_users():
#     response = client.get("/users")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# # Update a user
# def test_update_user():
#     response = client.put("/users/1", json=updated_user)
#     assert response.status_code == 200
#     assert response.json()["name"] == updated_user["name"]

# # Get a user by email
# def test_get_user_by_email():
#     response = client.get("/users/", params={"email": "john.doe@example.com"})
#     assert response.status_code == 200
#     assert response.json()["email"] == "john.doe@example.com"

# #  Delete a user
# def test_delete_user():
#     response = client.delete("/users/1")
#     assert response.status_code == 200
#     assert response.json() == {"message": "User deleted successfully."}
