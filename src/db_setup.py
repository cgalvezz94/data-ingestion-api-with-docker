import sqlite3
from .config import SQLITE_DB_PATH

def init_database():
    """Crea la base de datos y tablas si no existen."""
    conn = sqlite3.connect(SQLITE_DB_PATH)
    cur = conn.cursor()

    # Ejemplo: creación de tablas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            department TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            job TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS hired_employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            datetime TEXT NOT NULL,
            department_id INTEGER NOT NULL,
            job_id INTEGER NOT NULL,
            FOREIGN KEY(department_id) REFERENCES departments(id),
            FOREIGN KEY(job_id) REFERENCES jobs(id)
        )
    """)

    conn.commit()
    conn.close()
    print(f"Base de datos inicializada en {SQLITE_DB_PATH}")
