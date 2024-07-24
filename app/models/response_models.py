from typing import \
    Optional  # Importation de Optional pour définir des champs facultatifs

from pydantic import \
    BaseModel  # Importation de BaseModel depuis Pydantic pour créer des modèles de données


# Définition de la classe CommuneResponse en tant que modèle de données Pydantic
class CommuneResponse(BaseModel):
    """
    Modèle de réponse pour une commune.

    Attributes:
        code_postal (str): Le code postal de la commune.
        nom_commune_complet (str): Le nom complet de la commune.
        code_departement (Optional[int]): Le code du département de la commune (facultatif).
        nom_departement (Optional[str]): Le nom du département de la commune (facultatif).
    """
    code_postal: str  # Champ obligatoire pour le code postal de la commune
    nom_commune_complet: str  # Champ obligatoire pour le nom complet de la commune
    code_departement: Optional[int]  # Champ facultatif pour le code du département
    nom_departement: Optional[str]  # Champ facultatif pour le nom du département

    class Config:
        """
        Configuration du modèle.

        Attributes:
            orm_mode (bool): Active le mode ORM pour permettre la conversion depuis des objets ORM.
        """
        orm_mode = True  # Active le mode ORM pour permettre l'utilisation du modèle avec des ORM comme SQLAlchemy
