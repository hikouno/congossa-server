# congossa-server
Server and API implementation for Congossa app.

https://github.com/hikouno/congossa


# Installation

On utilise pour l'implémentation un serveur Apache 2 exécutant du PHP 7.0,
et une base de données MySQL.

Tuto sympa pour debian / ubuntu (remplacer php5 par php7 dans les noms de paquets) :
https://doc.ubuntu-fr.org/installer_un_serveur_debian

Je vous propose de configurer Apache pour que le serveur congossa soit accessible
en localhost sur le port **8111**.

# API

Je propose ici de se mettre d'accord sur l'API que l'on va utiliser à savoir:
nom des pages ; parametres, valeurs de retour..

**Insérer spécifications de l'API ici**

Pour l'instant pour tester une seule page d'API hello vous renvoie une
string statique au format JSON.

**Attention :** Pour des raisons de généricité on veut que nos pages d'api se finissent
sans extension (en particulier et par exemple on ne veut pas appeler ajouterMembre.php mais 
ajouterMembre pour des raisons de transparence par rapport au langage d'implémentation).
Il faut donc changer un petit peu la configuration de Apache pour lui dire d'interpréter le PHP
de tous les fichiers dans notre dossier d'api (par défaut seulement les .php et quelques autres le sont).

Aller donc dans la conf de apache et ajouter la clause ci dessous :

    # Congossa edit, interpret files without extension (for "generic" API..)
    <Directory chemin/vers/la/racine/de/votre/serveur/congossa-server>

        <FilesMatch ".+">
            SetHandler application/x-httpd-php
        </FilesMatch>

    </Directory>

Je l'ai ajouté moi dans le fichier (je suis sous linux) `/etc/apache2/mods-available/php7.0.conf` (il y a peut etre moyen
de faire plus propre, enfin c'est pas dégueu non plus).

Et ça interprétera tous les fichiers en php dans votre serveur congossa (seulement).

# Test installation

Si vous arrivez à avoir votre string au format JSON dans votre navigateur en
tapant http://localhost:8111/hello c'est bon pour l'installation du coup.

# Communication Application / Serveur

Maintenant que le serveur est en route, il faut pouvoir lui envoyer des requêtes HTTP
depuis l'application congossa pour les fonctions "backend".

Un problème qui se pose est que lors des tests de développement,
l'application ionic est "sandboxée" et donc ne voit pas à les autres ports locaux
à la machine (et ne voit donc pas notre serveur en localhost:8111).

Pour le rendre visible, il faut utiliser un proxy qui va être lui visible par l'appli
ionic sandboxée, et qui pourra rediriger ses requêtes vers notre serveur.

À ce sujet un article très très intéressant pour comprendre :
https://juristr.com/blog/2016/11/configure-proxy-api-angular-cli/

Et du coup dans ionic pour configurer ce proxy il faut rajouter quelques lignes
au `ionic.config.json` à la racine du projet ionic congossa.

Par exemple le mien a cette tête :

        {
          "name": "congossa",
          "app_id": "",
          "type": "ionic-angular",
          "proxies": [{
            "path": "/api",
            "proxyUrl": "http://localhost:8111"
          }],
          "integrations": {
            "cordova": {}
          }
        }

Ensuite le serveur sera visible depuis l'application.
(À suivre méthode codée pour faire des requêtes depuis l'apppli en Angular 2).

#Django

Pour lancer django depuis congossa-server:
1) installer django + python 
2) cd congossa
3) 
3) python manage.py runserver
4) ouvrir son navigateur favori a http://localhost:8000/$nomDunePage$

Pendant l implementation :
Dans ton folder
- Cr�er une appli: python manage.py startapp $nomFolder$
- modifier urls.py pour le routage des requetes
- modifier views.py pour l'exectuion des fonctions
- modifier models.py pour ajouter des tables dans la BDD

dans le folder congossa:
- dans urls.py ajouter dans urlpatterns :path('$nomFolder$', include('$nomFloder$.urls')),
Si t'ajoute des trucs dans la BDD
- dans settings.py ajouter dans installed apps '$nomFolder$.apps.$nomFolder$Config'

Apres l implementation :
1) Si modification sur la BDD: python manage.py makemigrations $nomFolder$
2) python manage.py migrate
3) python manage.py runserver
