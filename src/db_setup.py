# src/db_setup.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from .config import SQLALCHEMY_DATABASE_URL

# Model's declarative base
Base = declarative_base()

# Models
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, nullable=False)

    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"<Department(id={self.id}, department='{self.department}')>"

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, nullable=False)

    employees = relationship("Employee", back_populates="job")

    def __repr__(self):
        return f"<Job(id={self.id}, job='{self.job}')>"

class Employee(Base):
    __tablename__ = "hired_employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    hired_date = Column(DateTime, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    # ORM relationships for joins
    department = relationship("Department", back_populates="employees")
    job = relationship("Job", back_populates="employees")

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', department_id={self.department_id}, job_id={self.job_id})>"


# Creation of engine's connection
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Local session to work with DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Yields a SQLAlchemy session and ensures it is closed after use.
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creates all tables defined in the SQLAlchemy models if they do not exist.
def init_database():
    Base.metadata.create_all(bind=engine)
    print(f"Database created/updated at {SQLALCHEMY_DATABASE_URL}")