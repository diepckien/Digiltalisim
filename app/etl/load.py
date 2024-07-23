from sqlalchemy.orm import Session

from app.models.data_model import Commune


def load_data(data, db: Session):
    """
    Charge les données transformées dans la base de données.

    Args:
        data (list): Liste de dictionnaires contenant les données transformées.
        db (Session): Session de base de données SQLAlchemy.
    """
    
    # Parcourt chaque ligne des données transformées
    for row in data:
        # Crée une instance de Commune avec les données de la ligne actuelle
        commune = Commune(
            code_postal=row['code_postal'],
            nom_commune_complet=row['nom_commune_complet']
        )
        # Ajoute l'instance de Commune à la session de la base de données
        db.add(commune)
    
    # Valide toutes les modifications de la session et les enregistre dans la base de données
    db.commit()
