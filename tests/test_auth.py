from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup():
    response = client.post("/signup", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass"
    })
    # 200 if new user, 400 if already exists
    assert response.status_code in [200, 400]

def test_login():
    response = client.post("/login", data={
        "username": "testuser",
        "password": "testpass"  # match signup password
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_profile_protected_route():
    # Login first to get the token
    login_response = client.post("/login", data={
        "username": "testuser",
        "password": "testpass"
    })
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    # Access /profile with the token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/profile", headers=headers)
    assert response.status_code == 200
    assert "username" in response.json()
