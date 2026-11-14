from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="SHADOW API",
    description="AI-Powered Detection and Monitoring System",
    version="1.0.0"
)

app.include_router(router)

@app.get("/api/info")
def project_info():
    return {
        "project": "SHADOW",
        "version": "1.0.0",
        "status": "development"
    }