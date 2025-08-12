# tests/test_requirement_1.py

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_requirement_1_success():
    # Call the endpoint
    response = client.get("/metrics/sql1/")
    # Print error details if status code is not 200
    if response.status_code != 200:
        print("Error detail:", response.json())
    # Assert success status code
    assert response.status_code == 200
    # Optional: check if response contains 'data' key and is list
    json_data = response.json()
    assert "data" in json_data
    assert isinstance(json_data["data"], list)

