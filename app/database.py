import os

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Lire la variable d'environnement DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Vérifier que DATABASE_URL est définie
if DATABASE_URL is None:
    raise ValueError("La variable d'environnement DATABASE_URL doit être définie")

# Création de l'objet Engine pour la connexion à la base de données
engine = create_engine(DATABASE_URL)

# Création de la session locale pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définition de la classe Base pour les déclarations de modèles
Base = declarative_base()

# Importez les modèles pour qu'ils soient enregistrés avec la base
from app.models import data_model
