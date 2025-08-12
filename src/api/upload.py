from fastapi import APIRouter, HTTPException, Depends
import pandas as pd
from sqlalchemy.orm import Session
from src.config import CSV_DEPARTMENTS, CSV_HIRED_EMPLOYEES, CSV_JOBS
from src.db_setup import get_db_session, Department, Job, Employee  

router = APIRouter()

@router.post("/")
def upload_csv_data(db: Session = Depends(get_db_session)):
    try:
        # Read CSVs locally 
        departments_df = pd.read_csv(CSV_DEPARTMENTS, header=None, names=['id', 'department'])
        jobs_df = pd.read_csv(CSV_JOBS, header=None, names=['id', 'job'])
        employees_df = pd.read_csv(CSV_HIRED_EMPLOYEES, header=None, names=['id', 'name', 'hired_date', 'department_id', 'job_id'])

        # Datetime issue fixed
        employees_df['hired_date'] = pd.to_datetime(employees_df['hired_date'], utc=True)
        employees_df['hired_date'] = employees_df['hired_date'].dt.tz_localize(None)

        # Delete rows with NaN 
        employees_df = employees_df.dropna(subset=['id', 'job_id', 'department_id', 'hired_date','name'])

        # Cast as int
        employees_df['job_id'] = employees_df['job_id'].astype(int)
        employees_df['department_id'] = employees_df['department_id'].astype(int)
        employees_df['id'] = employees_df['id'].astype(int)

        # Cleaning data tables
        db.query(Department).delete()
        db.query(Job).delete()
        db.query(Employee).delete()
        db.commit()

        # Departaments insert, db.bulk_save_objects is better for big datasets
        for _, row in departments_df.iterrows():
            dept = Department(id=row['id'], department=row['department'])
            db.add(dept)

        # Jobs Insert, db.bulk_save_objects is better for big datasets
        for _, row in jobs_df.iterrows():
            job = Job(id=row['id'], job=row['job'])
            db.add(job)

        # Employees insert, db.bulk_save_objects is better for big datasets
        for _, row in employees_df.iterrows():
            emp = Employee(
                id=row['id'], 
                name=row['name'], 
                hired_date=row['hired_date'], 
                department_id=row['department_id'], 
                job_id=row['job_id']
            )
            db.add(emp)

        db.commit()
        return {"message": "CSV files loaded successfully."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))