import re
import unicodedata


def remove_accents(text):
    # Normaliser les caractères Unicode
    text = unicodedata.normalize('NFKD', text)
    # Supprimer les accents en convertissant les caractères Unicode en ASCII
    text = text.encode('ASCII', 'ignore').decode('ASCII')
    return text

def transform_data(data):
    transformed_data = []
    for row in data:
        transformed_row = {
            'code_postal': row['code_postal'] if row['code_postal'] else 'N/A',
            # Supprimer les accents mais garder les espaces, apostrophes, lettres, chiffres et traits d'union
            'nom_commune_complet': remove_accents(row['nom_commune_complet'] or 'N/A').upper(),
            'code_departement': row['code_departement'] if row['code_departement'] else 'N/A',
            'nom_departement': remove_accents(row['nom_departement'] or 'N/A').upper()
        }
        transformed_data.append(transformed_row)
    return transformed_data
