
from fastapi import FastAPI

app = FastAPI(
    title="SHADOW API",
    description="AI-Powered Detection and Monitoring System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "SHADOW",
        "message": "SHADOW Backend is running",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SHADOW Backend"
    }
