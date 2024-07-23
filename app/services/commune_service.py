from sqlalchemy.orm import Session

from app.models.data_model import Commune


def add_commune(db: Session, code_postal: str, nom_commune_complet: str, code_departement: str, nom_departement: str):
    """
    Ajoute une nouvelle commune à la base de données.

    Args:
        db (Session): Session de base de données SQLAlchemy.
        code_postal (str): Code postal de la commune.
        nom_commune_complet (str): Nom complet de la commune.
        code_departement (str): Code du département.
        nom_departement (str): Nom du département.
    """
    commune = Commune(
        code_postal=code_postal,
        nom_commune_complet=nom_commune_complet,
        code_departement=code_departement,
        nom_departement=nom_departement
    )
    db.add(commune)
    db.commit()

def update_commune(db: Session, nom_commune_complet: str, code_postal: str = None, code_departement: str = None, nom_departement: str = None):
    """
    Met à jour les informations d'une commune existante dans la base de données.

    Args:
        db (Session): Session de base de données SQLAlchemy.
        code_postal (str): Code postal de la commune à mettre à jour.
        nom_commune_complet (str, optional): Nouveau nom complet de la commune.
        code_departement (str, optional): Nouveau code du département.
        nom_departement (str, optional): Nouveau nom du département.
    
    Returns:
        Commune: La commune mise à jour.
    """
    commune = db.query(Commune).filter(Commune.nom_commune_complet == nom_commune_complet).first()
    if commune is None:
        return None
    if code_postal:
        commune.code_postal = code_postal
    if code_departement:
        commune.code_departement = code_departement
    if nom_departement:
        commune.nom_departement = nom_departement
    db.commit()
    return commune

def get_commune_by_name(db: Session, nom_commune_complet: str):
    """
    Récupère les informations d'une commune à partir de son nom complet.

    Args:
        db (Session): Session de base de données SQLAlchemy.
        nom_commune_complet (str): Nom complet de la commune.

    Returns:
        Commune: Les informations de la commune si trouvée, sinon None.
    """
    commune = db.query(Commune).filter(Commune.nom_commune_complet == nom_commune_complet).first()
    return commune
