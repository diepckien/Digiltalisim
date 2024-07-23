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

# Définition de la classe Commune comme modèle de table SQLAlchemy
class Commune(Base):
    __tablename__ = "communes"  # Nom de la table dans la base de données

    # Définition des colonnes de la table
    code_postal = Column(String(5), primary_key=True, index=True)  # Code postal comme clé primaire
    nom_commune_complet = Column(String(100))  # Nom complet de la commune
    code_departement = Column(Integer)  # Code du département
    nom_departement = Column(String(100))  # Nom du département

# Création de toutes les tables dans la base de données
Base.metadata.create_all(bind=engine)
