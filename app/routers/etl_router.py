from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.etl.extract import extract_data
from app.etl.load import load_data
from app.etl.transform import transform_data

router = APIRouter()

# Dépendance pour la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/run-etl/")
async def run_etl(db: Session = Depends(get_db)):
    """
    Extraction des données via l'URL:
    https://www.data.gouv.fr/fr/datasets/r/dbe8a621-a9c4-4bc3-9cae-be1699c5ff25

    Transformer les noms des communes en MAJ

    Charger les codes postaux et les noms des communes dans la BD

    Returns:
        dict: Message de succès.
    """
    # URL du fichier CSV
    url = "https://www.data.gouv.fr/fr/datasets/r/dbe8a621-a9c4-4bc3-9cae-be1699c5ff25"
    
    # Processus ETL
    data = extract_data(url)
    transformed_data = transform_data(data)
    load_data(transformed_data, db)
    
    return {"message": "Data successfully loaded"}
