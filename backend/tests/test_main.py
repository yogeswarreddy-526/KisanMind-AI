from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "Running"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_about_endpoint():
    response = client.get("/about")

    assert response.status_code == 200
    assert response.json()["name"] == "KisanMind AI"