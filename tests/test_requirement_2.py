# tests/test_requirement_2.py

import pytest
from fastapi.testclient import TestClient
from src.main import app  # Ajusta el import según tu estructura real

client = TestClient(app)

def test_get_requirement_2_success():
    # Realiza una petición GET al endpoint de requirement_2
    response = client.get("/metrics/sql2/")
    
    # Si falla, imprime el detalle para debugging
    if response.status_code != 200:
        print("Error detail:", response.json())
    
    # Verifica que la respuesta fue exitosa
    assert response.status_code == 200
    
    # Verifica que la respuesta tenga la clave "data" y sea una lista
    json_response = response.json()
    assert "data" in json_response
    assert isinstance(json_response["data"], list)
