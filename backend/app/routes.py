from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "project": "SHADOW",
        "message": "SHADOW Backend API",
        "status": "success"
    }

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SHADOW Backend"
    }