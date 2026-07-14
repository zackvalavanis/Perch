from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db

client = TestClient(app)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# def test_get_user():
#     response = client.get('/user/{id}')
#     assert response.status_code == 200
