from fastapi import APIRouter
from src.birthday.index import router as birthdays_router
from src.health.index import router as health_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(birthdays_router)