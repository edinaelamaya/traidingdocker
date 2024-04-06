from fastapi import APIRouter, Depends

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from app.main import app

docs = APIRouter()

@docs.get("/documentation", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

@docs.get("/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(title = "FastAPI", version="0.1.0", routes=app.routes)