import requests  # Importation de la bibliothèque requests pour effectuer des requêtes HTTP


def get_coordinates(city_name: str):
    # Définir l'URL de l'API de géocodage
    url = 'http://localhost:8080/search'
    
    # Définir les paramètres de la requête
    params = {
        'q': city_name,  # Nom de la ville à rechercher
        'format': 'json',  # Format de la réponse attendu (JSON)
        'limit': 1  # Limiter le nombre de résultats à 1
    }
    
    # Envoyer une requête GET à l'API avec les paramètres spécifiés
    response = requests.get(url, params=params)
    
    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Convertir la réponse JSON en dictionnaire Python
        data = response.json()
        
        # Vérifier si des données ont été retournées
        if data:
            # Extraire la latitude et la longitude du premier résultat
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            # Retourner la latitude et la longitude
            return latitude, longitude
    else:
        # Afficher un message d'erreur si le code de statut n'est pas 200
        print(f"Error: Received status code {response.status_code}")
        print(response.text)
    
    # Retourner None, None si aucune coordonnée n'a été trouvée ou en cas d'erreur
    return None, None
