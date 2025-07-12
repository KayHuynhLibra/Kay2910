from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()
    assert "docs_url" in response.json()

def test_login():
    response = client.post(
        "/api/v1/token",
        data={"username": "testuser", "password": "password"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_wrong_password():
    response = client.post(
        "/api/v1/token",
        data={"username": "testuser", "password": "wrongpassword"}
    )
    assert response.status_code == 401

def test_read_users_me():
    # First login to get token
    login_response = client.post(
        "/api/v1/token",
        data={"username": "testuser", "password": "password"}
    )
    token = login_response.json()["access_token"]
    
    # Then try to get user info
    response = client.get(
        "/api/v1/users/me/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert "username" in response.json()
    assert "email" in response.json() 