from sqlalchemy import Column, Integer, String

from app.database import Base, engine


# Définition de la classe Commune comme modèle de table SQLAlchemy
class Commune(Base):
    __tablename__ = "communes"  # Nom de la table dans la base de données

    # Définition des colonnes de la table
    id = Column(Integer, primary_key=True, autoincrement=True)  # Clé primaire auto-incrémentée
    code_postal = Column(String(5)) # Code postal
    nom_commune_complet = Column(String(100))  # Nom complet de la commune
    code_departement = Column(Integer)  # Code du département
    nom_departement = Column(String(100))  # Nom du département

# Création de toutes les tables dans la base de données
Base.metadata.create_all(bind=engine)
