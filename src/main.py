from fastapi import FastAPI
from src.api import upload, batch_insert, requirement_1, requirement_2  

app = FastAPI(
    title="Data Ingestion API",
    description="API for uploading CSV data and querying SQL metrics",
    version="1.0.0"
)


app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(batch_insert.router, prefix="/batch", tags=["Batch Insert"])
app.include_router(requirement_1.router, prefix="/metrics/sql1", tags=["Requirement 1"])
app.include_router(requirement_2.router, prefix="/metrics/sql2", tags=["Requirement 2"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
