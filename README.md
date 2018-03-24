# Projet Velib

## Description

Le projet consiste à récupérer des données en temps réel des API concernant les velibs (puis ceux de la météo, du trafic routier, des transports, des manifestations culturelles) afin de pouvoir faire une prédiction du nombre de vélo à disposition ou manquant par station pour un jour et une heure donnée.

## Target
### Cible marketing
- JCDecaux, entreprise proposant des Velib
### Cibles utilisatrices
- Les usagers du Velib
- Le personnel de JCDecaux pour la redistribution des vélos
- Les entreprises partenaires/concurrentes du Velib
- Les services publiques des villes concernées

## Insights
- quelles sont les stations les plus demandées pour les velib au cours du temps ?
- quelles sont bornes les plus demandées au cours du temps ?
- quel est le plus court chemin pour remplir les stations de manière optimale ?
- quel est le plus court chemin pour se rendre à une destination ayant à proximité, une station de vélo avec des bornes libres ?
- dans quels quartiers y a t-il le plus d'usager de vélib ? et à quels moments de la journée ?

## Valeur ajoutée
### Pour JCDecaux
- prévoir un planning optimisé (+ court chemin) à de réapprovisionnement et de redistribution de vélos d'après le % de vélo manquant par station qui varie selon la météo, le trafic routier, état des transports (métro, RER) et des manifestations culturelles = gain d'efficacité + économies sur les promotions proposées aux usagers

### Pour les usagers
- prévoir à un jour et une heure donnée si :
  - un vélo sera disponible à la station demandée
  - une borne sera disponible à la station d'arrivée
- bénéficier de promotions sur l'utilisation des Velib ou des entreprises partenaires à proximités lorsque les camions de redistribution sont déjà passés et qu'il manque des vélos à une station donnée

### Pour les entreprises concurrentes qui peuvent devenir partenaires (entreprise de vélos-taxis, scooter, restaurateurs, ...)
- prévoir les stations en rupture de vélos pour pouvoir proposer leurs services 
  - être physiquement au bon moment au bon endroit
  - faire du marketing ciblé (SEA sur google, publication facebook sponsorisée) selon le lieu géographique 
  => le marketing pourra être affiné dans la version V2 du projet si on peut récupérer des données anonymisées sur les usagers du Velib

### Service public 
- mieux gérer les flux de circulation de la ville
- proposer un service moins polluant et plus accessible lors d'une manifestation culturelle
- suggérer des itinéraires touristiques avec l'assurance d'avoir des vélos et des bornes disponibles au moment souhaité


# Pipeline big data
## Architecture
![](https://github.com/ctith/Projet_Velib/blob/master/Diagrammes/pipelineBD.svg)

## Outils
Utilisation de Talend Open Studio pour :
  - collecter les données depuis les API REST
  - les faire transiter avec Kafka
  - qui les enverra à HDFS pour les stocker

### Data Sources
Récupération des données sous forme JSON depuis les API REST 

### Data Ingest
Utilisation de Kafka plutôt que de Flume car :
- https://blog.octo.com/introduction-a-flume-ng/ 
- pas de composants Flume disponibles sur Talend Open Studio (TOS) donc pour des raisons liées au budget, au temps imparti et aux compétences techniques de l'équipe, il vaut mieux utiliser Kafka via TOS.
- on n'utilise pas Spark Streaming car si HDFS devait être indisponible, on perdrait des données alors qu'avec le système de réplication et distribution de données de Kafka (partitions), les données seront sauvegardées le temps que HDFS se remette en route.

### Data Storage
Utilisation de HDFS pour pouvoir stocker les données et permettre à Spark de les traiter là où elles se trouvent
- on n'utilise pas Cassandra car même si la BDD permet d'avoir un schéma de données qui vérifie le type de donnée inséré et garantit ainsi la véracité des données, le modèle est figé et ne permet pas un scalabilité du projet.
- on n'utilise pas MongoDB car même si la BDD permet de stocker et d'effectuer des traitements sur les données, il aurait fallu faire importer ces données vers HDFS pour pouvoir les traiter avec Spark. On peut légitimer l'utilisation de MongoDB en tant que BDD backup du projet.

### Data Processing
Utilisation de Spark
- Spark SQL pour effectuer des requêtes
- Spark ML pour réaliser des modèles prédictifs et de la visualisation 
  
### Data Vizualisation 
Utilisation de D3JS pour la visualisation des données

## Traitement de la donnée
### Collecte
- open data donc pas de data compliance ni de RGPD 
- pas de web scrapping nécessaire
- Les données sont en JSON comme elles proviennent des APIs

### Intégration
Pas de nettoyage des données ni d’anonymisation à effectuer car open data

### Stockage
Document JSON sous forme de clé-valeur permettant l'aggrégation de données mais ayant pour inconvénient :
  - la hiérarchisation des accès : certaines données sont plus accessibles que d'autres selon leur niveau d'imbrication dans le document
  - la perte d’autonomie des entités : il n'est pas possible de supprimer un élément sans supprimer entièrement le reste du document
  - la redondance: les données statiques sont représentées plusieurs fois
  
# Sources de données
- [API Velib - temps réel](https://developer.jcdecaux.com/#/opendata/vls?page=dynamic)
- [API Météo - temps réel et prévisions](https://openweathermap.org/api)
- [API STIF - temps réel](https://opendata.stif.info/page/home/)
- [API Trafic routier - temps réel](https://opendata.paris.fr/explore/dataset/comptages-routiers-permanents/information/)
- [API Movement uber](https://d3i4yxtzktqr9n.cloudfront.net/web-movement/static/pdfs/Movement-TravelTimesMethodology-76002ded22.pdf)
- [API Manifestation sportives](https://www.manifestationsportive.fr/api/)
- [API Evenements](https://openagenda.zendesk.com/hc/fr/categories/115000324454-API)
- [API Salles et festivals](http://www.sowprog.com/api/)
- [API Paris Events](https://opendata.paris.fr/explore/dataset/evenements-a-paris/?disjunctive.tags&disjunctive.placename&disjunctive.city)
