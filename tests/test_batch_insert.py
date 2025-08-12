import pytest
from fastapi.testclient import TestClient
from src.main import app  # Asumiendo que tu FastAPI app está en src/main.py
from src.db_setup import get_db_session, Employee

client = TestClient(app)

# Fixture para limpiar la tabla Employee antes y después de cada test
@pytest.fixture(autouse=True)
def clear_employees_between_tests():
    db = next(get_db_session())
    # Limpia antes del test
    db.query(Employee).delete()
    db.commit()
    yield
    # Limpia después del test
    db.query(Employee).delete()
    db.commit()

valid_payload = {
    "employees": [
        {
            "id": 1,
            "name": "John Doe",
            "hired_date": "2024-01-15T00:00:00",
            "department_id": 10,
            "job_id": 3
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "hired_date": "2024-02-20T00:00:00",
            "department_id": 12,
            "job_id": 4
        }
    ]
}

def test_batch_insert_success():
    # Test successful insertion of employees batch
    response = client.post("/batch/", json=valid_payload)
    if response.status_code != 200:
        print("Error response JSON:", response.json())  # Print error details if fails
    assert response.status_code == 200
    assert response.json() == {"message": "2 employees inserted successfully."}

def test_batch_insert_empty_list():
    # Test error when sending empty employees list (should fail validation)
    response = client.post("/batch/", json={"employees": []})
    assert response.status_code == 422  # Unprocessable Entity (validation error)

def test_batch_insert_missing_field():
    # Test error when a required field is missing
    invalid_payload = {
        "employees": [
            {
                "id": 1,
                # "name" missing here
                "hired_date": "2024-01-15T00:00:00",
                "department_id": 10,
                "job_id": 3
            }
        ]
    }
    response = client.post("/batch/", json=invalid_payload)
    assert response.status_code == 422  # Validation error for missing field

