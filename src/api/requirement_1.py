from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db_setup import get_db_session
from src.config import SQL_REQUIREMENT_1_PATH

router = APIRouter()

@router.get("/")
def get_requirement_1(db: Session = Depends(get_db_session)):
    try:
        # Read SQL 1
        with open(SQL_REQUIREMENT_1_PATH, "r") as file:
            query = file.read()

        # Execution of raw query
        result = db.execute(query)

        # Convert result to dictionary list
        rows = [dict(row) for row in result.fetchall()]

        return {"data": rows}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
