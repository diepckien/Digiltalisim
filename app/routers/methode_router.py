from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.services.commune_service import (add_commune, get_commune_by_name,
                                          update_commune)

router = APIRouter()

# Dépendance pour obtenir la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/communes/")
async def push_commune(code_postal: str, nom_commune_complet: str, code_departement: str, nom_departement: str, db: Session = Depends(get_db)):
    """
    Ajoute une nouvelle commune à la base de données.

    Args:
        code_postal (str): Code postal de la commune.
        nom_commune_complet (str): Nom complet de la commune.
        code_departement (str): Code du département.
        nom_departement (str): Nom du département.
        db (Session): Session de base de données SQLAlchemy.

    Returns:
        dict: Message de succès.
    """
    add_commune(db, code_postal, nom_commune_complet, code_departement, nom_departement)
    return {"message": "Commune added successfully"}

@router.put("/communes/{nom_commune_complet}")
async def update_commune_endpoint(nom_commune_complet: str, code_postal: str = None, code_departement: str = None, nom_departement: str = None, db: Session = Depends(get_db)):
    """
    Met à jour les informations d'une commune existante dans la base de données.

    Args:
        code_postal (str): Code postal de la commune à mettre à jour.
        nom_commune_complet (str, optional): Nouveau nom complet de la commune.
        code_departement (str, optional): Nouveau code du département.
        nom_departement (str, optional): Nouveau nom du département.
        db (Session): Session de base de données SQLAlchemy.

    Returns:
        dict: Message de succès ou erreur si la commune n'existe pas.
    """
    commune = update_commune(db, nom_commune_complet, code_postal, code_departement, nom_departement)
    if commune is None:
        raise HTTPException(status_code=404, detail="Commune not found")
    return {"message": "Commune updated successfully"}

@router.get("/commune/{nom_commune_complet}")
async def retrieve_commune(nom_commune_complet: str, db: Session = Depends(get_db)):
    """
    Récupère les informations d'une commune en fonction de son nom complet.

    Args:
        nom_commune_complet (str): Nom complet de la commune.
        db (Session): Session de base de données SQLAlchemy.

    Returns:
        Commune: Les informations de la commune si trouvée, sinon une erreur.
    """
    commune = get_commune_by_name(db, nom_commune_complet)
    if commune is None:
        raise HTTPException(status_code=404, detail="Commune not found")
    return {
        "code_postal": commune.code_postal,
        "nom_commune_complet": commune.nom_commune_complet,
        "code_departement": commune.code_departement,
        "nom_departement": commune.nom_departement
    }
