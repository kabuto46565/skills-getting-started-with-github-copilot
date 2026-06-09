from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_read_main():
    # Arrange & Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
