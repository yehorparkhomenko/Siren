from fastapi import FastAPI
from src.siren.config.routes import api_router
from src.siren.config.settings import settings


def get_app():
    app = FastAPI(title=settings.PROJECT_NAME, openapi_url="/api/v1/openapi.json")
    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app
