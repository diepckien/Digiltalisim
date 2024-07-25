# Definition de l'application

Cette application est une API web construite avec FastAPI et une base de données Mysql, conçue pour fournir des informations géographiques et administratives sur les communes françaises.

## Fonctionnalités Principales

### Recherche de Communes :

- Permet de rechercher des communes françaises par leur nom.
- Retourne les informations telles que le code postal, le nom complet de la commune, le code et le nom du département.

### Géocodage :

- Intègre un service de géocodage utilisant Nominatim pour obtenir les coordonnées GPS (latitude et longitude) d'une ville donnée.

### ETL :

- Un module ETL peut être inclus pour extraire, transformer et charger des données spécifiques à l'application.

### Exportation des Métriques :

- Expose des métriques pour la surveillance et l'analyse des performances via Prometheus.

## Composants Principaux

### Base de Données :

- Utilise MySQL pour stocker les données des communes.
- Initialise la base de données avec un script init-db.sql lors du démarrage.

### ORM (Object-Relational Mapping) :

- Utilise SQLAlchemy pour mapper les objets Python aux tables de la base de données.
- Définit un modèle de données Commune avec des champs comme code_postal, nom_commune_complet, code_departement, et nom_departement.

### Routes de l'API :

- ETL Router : Pour les opérations ETL.
- Geocoding Router : Pour les opérations de géocodage.
- Methode Router : Pour d'autres méthodes spécifiques à l'application.

### Sécurité et Permissions :

- Exécute le conteneur Docker avec un utilisateur non-root pour des raisons de sécurité.

### Docker et Docker Compose :

- Utilise Docker Compose pour orchestrer les différents services (application web, base de données, service de géocodage).

# Comment utiliser ce programme

## Lancer les services un par un
- Lancer la geoloc service :

sudo docker run -it   -e PBF_URL=https://download.geofabrik.de/europe/monaco-latest.osm.pbf   -e REPLICATION_URL=https://download.geofabrik.de/europe/monaco-updates/   -p 8080:8080   --name nominatim   mediagis/nominatim:4.4

- Lancer la Base de données :

sudo docker run  -v /repos/db/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -d mysql:5.7

- Lancer l'application :

uvicorn app.main:app --reload

## Lancer tous les services en même temps avec docker-compose

- Demarrer tous les services :

sudo docker-compose up -d

- Arret tous les servcies :

sudo docker-compose down

## Accès à l'API Documentation Interactive

* Utilisez Swagger UI disponible à http://localhost:8000/docs pour tester et interagir avec les endpoints de l'API.
* Utilisez Redoc disponible à http://localhost:8000/redoc pour une documentation alternative de l'API.

# Comment lancer les tests
- Exporter les variables environnement, lancer à la racine du projet la commande suivante: . .env.sh
- Lancer la commande : pytest -v

