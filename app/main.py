from fastapi import FastAPI

from app.routers import etl_router, methode_router

app = FastAPI()

# Inclure les routeurs
app.include_router(etl_router.router, prefix="/etl", tags=["ETL"])

app.include_router(methode_router.router, prefix="/methode", tags=["METHODE"])