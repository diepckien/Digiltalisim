from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.etl.extract import extract_data
from app.etl.transform import transform_data

# from app.etl.load import load_data

app = FastAPI()

# Dépendance pour la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/run-etl/")
async def run_etl(db: Session = Depends(get_db)):
    # URL du fichier CSV
    url = "https://www.data.gouv.fr/fr/datasets/r/dbe8a621-a9c4-4bc3-9cae-be1699c5ff25"
    
    # Processus ETL
    data = extract_data(url)
    transformed_data = transform_data(data)
    for row in transformed_data[:5]:  # Affiche les 5 premières lignes de données
        print(row)
    # load_data(transformed_data, db)
    
    return {"message": "Data successfully loaded"}
