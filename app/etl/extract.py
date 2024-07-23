import csv
from io import StringIO

import requests


def extract_data(url: str):
    try:
        # Télécharger le contenu CSV depuis l'URL
        response = requests.get(url)
        response.raise_for_status()  # Vérifie que la requête a réussi

        # Lire le contenu CSV en mémoire
        csv_content = StringIO(response.text)
        
        # Utiliser DictReader pour lire les données CSV
        reader = csv.DictReader(csv_content)
        data = [row for row in reader]
        
        return data
    except requests.exceptions.RequestException as e:
        # Gérer les exceptions (erreurs de connexion, erreurs HTTP, etc.)
        print(f"Erreur lors de la récupération des données : {e}")
        return None, None
    except csv.Error as e:
        print(f"Erreur lors de l'analyse du fichier CSV : {e}")
        return None, None


