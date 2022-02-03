from workshop.app import app
from fastapi.testclient import TestClient


def test_get_uselist(temp_db):
    request_data = {
        "email": "vader@deathstar.com",
        "name": "Darth Vader",
        "password": "rainbow"
    }
    with TestClient(app) as client:
        response = client.post("/user-list", json=request_data)
    assert response.status_code == 200


def test_get_usen(temp_db):
    with TestClient(app) as client:
        response = client.get("/user/2")
    assert response.status_code == 404
