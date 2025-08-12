from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db_setup import get_db_session
from src.config import SQL_REQUIREMENT_2_PATH

router = APIRouter()

@router.get("/")
def get_requirement_2(db: Session = Depends(get_db_session)):
    try:
        # Leer el script SQL
        with open(SQL_REQUIREMENT_2_PATH, "r") as file:
            query = file.read()

        # Ejecutar el query raw
        result = db.execute(query)

        # Convertir resultado a lista de diccionarios
        rows = [dict(row) for row in result]

        return {"data": rows}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
