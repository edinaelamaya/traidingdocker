from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
from app.routers.docs import docs
from app.routers.get_data import get_nombre
from datetime import datetime


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(docs)
app.include_router(get_nombre)

@app.get("/", tags=['Home'])
async def get_status():
    return {}