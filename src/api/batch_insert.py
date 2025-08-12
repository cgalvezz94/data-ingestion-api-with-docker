# src/api/batch_insert.py

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List
from sqlalchemy.orm import Session
from src.db_setup import get_db_session, Employee

router = APIRouter()

# We define the Pydantic model to validate each employee received
class EmployeeBatchInsert(BaseModel):
    id: int
    name: str
    hired_date: str
    department_id: int
    job_id: int

# The body will be a list with a minimum of 1 and a maximum of 1000 employees
class EmployeeBatchRequest(BaseModel):
    employees: List[EmployeeBatchInsert] = Field(..., min_items=1, max_items=1000)

@router.post("/")
def batch_insert(data: EmployeeBatchRequest, db: Session = Depends(get_db_session)):
    try:
        # Convert each employee to an ORM Employee model
        employees_to_add = [
            Employee(
                id=emp.id,
                name=emp.name,
                datetime=emp.hired_date,
                department_id=emp.department_id,
                job_id=emp.job_id
            )
            for emp in data.employees
        ]

        db.bulk_save_objects(employees_to_add)
        db.commit()

        return {"message": f"{len(employees_to_add)} employees inserted successfully."}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
