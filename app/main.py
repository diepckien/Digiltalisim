from fastapi import FastAPI

from app.routers import etl_router

app = FastAPI()

# Inclure les routeurs
app.include_router(etl_router.router, prefix="/etl", tags=["ETL"])

