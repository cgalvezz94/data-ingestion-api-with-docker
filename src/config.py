import os

# Where config.py is
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Where CSVs and db are 
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