from fastapi import (  # Importation des classes APIRouter et HTTPException depuis FastAPI
    APIRouter, HTTPException)

from app.services.geocoding_service import \
    get_coordinates  # Importation de la fonction get_coordinates depuis le service de géocodage

# Création d'un routeur API pour organiser les routes de l'application
router = APIRouter()

@router.get("/geocode/{city_name}")
def geocode_city(city_name: str):
    """
    Récupère les coordonnées géographiques d'une ville.

    Args:
        city_name (str): Le nom de la ville pour laquelle récupérer les coordonnées.

    Returns:
        dict: Un dictionnaire contenant le nom de la ville, la latitude et la longitude.

    Raises:
        HTTPException: Si les coordonnées de la ville ne sont pas trouvées, une exception HTTP 404 est levée.
    """
    # Appel de la fonction get_coordinates pour obtenir la latitude et la longitude de la ville
    lat, lon = get_coordinates(city_name)
    
    # Vérification si les coordonnées sont trouvées
    if lat is None or lon is None:
        # Lève une exception HTTP 404 si les coordonnées ne sont pas trouvées
        raise HTTPException(status_code=404, detail="Coordinates not found for the city")
    
    # Retourne un dictionnaire contenant le nom de la ville, la latitude et la longitude
    return {"city": city_name, "latitude": lat, "longitude": lon}
