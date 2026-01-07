from fastapi import APIRouter
from src.entrypoints.default_handlers import router as health_router

router = APIRouter()
router.include_router(health_router)