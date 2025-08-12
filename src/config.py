import os

# Detectar si estamos ejecutando pytest
IS_TEST = "PYTEST_CURRENT_TEST" in os.environ

# Where config.py is
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DATA directory (diferente si es test)
if IS_TEST:
    DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "tests", "data"))
else:
    DATA_DIR = os.path.join(BASE_DIR, "data")

# Full path to SQLite file
SQLITE_DB_PATH = os.path.join(DATA_DIR, "database.db")

# URL de conexión para SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQLITE_DB_PATH}"

# CSV paths
CSV_DEPARTMENTS = os.path.join(DATA_DIR, "departments.csv")
CSV_HIRED_EMPLOYEES = os.path.join(DATA_DIR, "hired_employees.csv")
CSV_JOBS = os.path.join(DATA_DIR, "jobs.csv")

# Batch insert max rows
BATCH_SIZE = 1000

# SQL script paths
SQL_REQUIREMENT_1_PATH = os.path.join(BASE_DIR, "sql", "requirement_1.sql")
SQL_REQUIREMENT_2_PATH = os.path.join(BASE_DIR, "sql", "requirement_2.sql")
