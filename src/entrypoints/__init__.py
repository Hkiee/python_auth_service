from fastapi import APIRouter
from src.entrypoints.default_handlers.health_check import router as health_router

router = APIRouter()
router.include_router(health_router)