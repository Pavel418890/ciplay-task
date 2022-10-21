from fastapi import FastAPI

from app.api.v1 import api
from app.core.config import config

app = FastAPI(openapi_url=f"{config.API_V1}/openapi.json")

app.include_router(router=api.api_router, prefix=config.API_V1)
