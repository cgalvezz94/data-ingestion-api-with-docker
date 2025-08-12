import os
import shutil
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.config import CSV_DEPARTMENTS, CSV_HIRED_EMPLOYEES, CSV_JOBS
from src.db_setup import init_database

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_env():
    # Crear tablas en la base de datos
    init_database()

    # Crear carpeta destino si no existe
    os.makedirs(os.path.dirname(CSV_DEPARTMENTS), exist_ok=True)

    # Copiar CSV desde tests/data a las rutas esperadas
    test_data_dir = os.path.join(os.path.dirname(__file__), "data")

    shutil.copy(os.path.join(test_data_dir, "departments.csv"), CSV_DEPARTMENTS)
    shutil.copy(os.path.join(test_data_dir, "jobs.csv"), CSV_JOBS)
    shutil.copy(os.path.join(test_data_dir, "hired_employees.csv"), CSV_HIRED_EMPLOYEES)

    yield

    # Limpieza opcional
    for f in [CSV_DEPARTMENTS, CSV_JOBS, CSV_HIRED_EMPLOYEES]:
        if os.path.exists(f):
            os.remove(f)

def test_upload_csv_success():
    response = client.post("/upload/")
    if response.status_code != 200:
        print("ERROR RESPONSE:", response.text)
    assert response.status_code == 200
    assert response.json()["message"] == "CSV files loaded successfully."






