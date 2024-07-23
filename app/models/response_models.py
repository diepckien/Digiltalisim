from typing import Optional

from pydantic import BaseModel


class CommuneResponse(BaseModel):
    code_postal: str
    nom_commune_complet: str
    code_departement: Optional[int]
    nom_departement: Optional[str]

    class Config:
        orm_mode = True
