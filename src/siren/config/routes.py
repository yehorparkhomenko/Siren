from fastapi import APIRouter

from src.siren.ui.http.application import common
from src.siren.ui.http.user import user

api_router = APIRouter()
api_router.include_router(common.router, tags=["Common"])
api_router.include_router(user.router, tags=["User"])
