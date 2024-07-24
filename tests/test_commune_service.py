import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.data_model import Base, Commune
from app.services.commune_service import get_communes_by_departement

# Configuration de la base de données de test
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Utiliser une base de données SQLite en mémoire pour les tests
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Création de la base de données de test
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    """
    Fixture pour obtenir une session de base de données de test.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def setup_db(db):
    """
    Fixture pour configurer la base de données avec des données de test.
    """
    # Ajouter des communes de test
    commune1 = Commune(code_postal="1400", nom_commune_complet="L'ABERGEMENT-CLÉMENCIAT", code_departement=1, nom_departement="Ain")
    commune2 = Commune(code_postal="1640", nom_commune_complet="L'ABERGEMENT-DE-VAREY", code_departement=1, nom_departement="Ain")
    db.add(commune1)
    db.add(commune2)
    db.commit()

def test_get_communes_by_departement(db, setup_db):
    """
    Test pour la fonction get_communes_by_departement.
    """
    communes = get_communes_by_departement(db, 1)
    assert len(communes) == 2
    assert communes[0].nom_commune_complet == "L'ABERGEMENT-CLÉMENCIAT"
    assert communes[1].nom_commune_complet == "L'ABERGEMENT-DE-VAREY"
