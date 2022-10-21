from fastapi import APIRouter

from app.api.v1.endpoints import stats

api_router = APIRouter()
api_router.include_router(router=stats.router, prefix="/stats", tags=["stats"])
