# Comment utiliser ce programme

- Lancer la geoloc service :

sudo docker run -it   -e PBF_URL=https://download.geofabrik.de/europe/monaco-latest.osm.pbf   -e REPLICATION_URL=https://download.geofabrik.de/europe/monaco-updates/   -p 8080:8080   --name nominatim   mediagis/nominatim:4.4

- Lancer la Base de données :

sudo docker run  -v /repos/db/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -d mysql:5.7

- Lancer l'application :

uvicorn app.main:app --reload

# Comment lancer les tests
- Exporter les variables environnement, lancer à la racine du projet la commande suivante: . .env.sh
- Lancer la commande : pytest -v

