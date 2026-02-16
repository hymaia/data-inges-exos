# Config by Hymaia

Tout se fait en Python

## Objectif

L'objectif de l'exercice est d'apprendre à bien gérer sa configuration dans son application. Plusieurs méthodes seront mises en pratique :
* Les paramètres de main
* Le fichier de conf
* Les variables d'environnement
* Les parameters store et secret managers

## Les techniques simples

### Paramètres de main

Utilisez `argsparse` pour créer une application simple qui lit 3 arguments :
* dh-host : Database host
* db-port : Database port
* api-key : API key

Et qui affiche les valeurs.

### Fichier de configuration

Utilisez `pyyaml` pour créer une application simple qui lit un fichier de conf au format yaml avec 3 valeurs :
* dh_host : Database host
* db_port : Database port
* api_key : API key

Et qui affiche les valeurs.

### Variable d'environnement

Utilisez les variables d'environnement pour créer une application simple qui lit un fichier de conf au format yaml avec 3 valeurs :
* dh_host : Database host
* db_port : Database port
* api_key : API key

Et qui affiche les valeurs.

Vous pouvez utiliser dotenv.

## Utiliser un service externe de configuration

Il existe des services de configuration nommés secret manager ou parameter store qui servent à stocker nos paramètres, sensible ou non, de nos applications.

### Parameter store : exemple avec AWS

Sur AWS le parameter store s'appelle.... Parameter Store

Créez une lambda qui va aller chercher sa configuration dans un parameter store et affichez les valeurs :
* dh_host : Database host
* db_port : Database port


### Secret manager : exemple avec AWS

Sur AWS le secret manager s'appelle.... Secret Manager

Ajoutez à votre lambda la lecture d'un secret pour l'API key et affichez la valeur.

## Créer le meilleur des mondes

Créer une factory de lecture de config qui permet de récupérer les paramètres qu'il soit en environnement, dans un secret manager ou dans un parameter store.

L'interface pour le reste de l'application doit être agnostique et accessible depuis partout. 
