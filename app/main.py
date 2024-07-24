from fastapi import FastAPI  # Importation de la classe FastAPI depuis FastAPI

from app.routers import (  # Importation des routeurs définis dans le projet
    etl_router, geocoding_router, methode_router)

# Création d'une instance de l'application FastAPI
app = FastAPI()

# Inclure les routeurs
app.include_router(etl_router.router, prefix="/etl", tags=["ETL"])
"""
Inclut le routeur ETL dans l'application avec le préfixe "/etl".
Les routes définies dans ce routeur seront accessibles via "/etl".
"""

app.include_router(methode_router.router, prefix="/methode", tags=["METHODE"])
"""
Inclut le routeur des méthodes dans l'application avec le préfixe "/methode".
Les routes définies dans ce routeur seront accessibles via "/methode".
"""

app.include_router(geocoding_router.router, prefix="/geocoding", tags=["GEOCODING"])
"""
Inclut le routeur de géocodage dans l'application avec le préfixe "/geocoding".
Les routes définies dans ce routeur seront accessibles via "/geocoding".
Les routes sont étiquetées avec le tag "GEOCODING" pour une meilleure organisation et documentation.
"""
