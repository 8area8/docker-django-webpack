# Docker Django Webpack

>Note : actuellement en français  

---

## 1 - Les Technologies

### a. L'architecture de Docker-compose
- Nginx (connexion sécurisée en locale et en production avec mkcert et certbot, à implémenter soi même)
- Django Gunicorn
- Redis
- PostgreSQL (**pour le developpement**)
- Selenium et Selenium-chrome (**pour le developpement**)

### b. L'architecture de l'application backend

- Django-otp : gère la "Two Factor Authentication" pour le compte admin
- Django-debug-toolbar : panneau latéral de'informations
- Django-redis : implémentation de Redis en cache
- Selenium : pour les tests fonctionnels
- Django Unittest : pour les tests unitaires et fonctionnels

### c. L'architecture de l'application front-end

- NPM et Webpack
- Typescript et SCSS
- PugJs
- Jest

<!-- - Bulma (framework SASS) -->

### d. L'architecture de versionning

<!-- - OVH UX Flow (workflow) -->

- travis

---

## 2 - Installation

### a. Préréquis

- posséder docker et docker-compose (docker-compose v3.7)
- Facultatif : posséder npm (nodeJs) intégré dans votre *Path* (pour les tests).
- Facultatif : posséder VNC viewer (pour visualiser les tests Selenium).

### b. La commande d'installation

- Lancer `. run setup` dans votre shell bash depuis la raçine du projet.

---

## 3 - Commandes De Lancement

>Ces commandes sont à entrer dans votre Shell bash à la racine du projet.

### Le projet

- Lancer le projet : `. run UP`. L'application est accessible depuis l'adresse `127.0.0.1`.

### Les tests

> Le tests Django et Selenium ne peuvent se lancer qui si les conteneurs sont en fonction.

- Lancer les tests Selenium : `. run djselenium`. Voir la partie "Selenium" pour visualiser les tests avec VNC Viewer.
- Lancer les autres tests django : `. run djtest`.
- Lancer les tests Jest : `. run ntest`.

---

## 4 - Selenium

Pour visualiser les tests Selenium, installez *VNC Viewer*.  
Ouvrez ensuite VNC Viewer et ajoutez une nouvelle connexion (fichier - Nouvelle connexion).  
Remplissez les champs comme dans l'exemple:  
  
![VNC Viewer example](https://i.imgur.com/9Y9DPkn.png)
  
Lancez les conteneurs si ce n'est pas déjà fait.  
Ouvrez ensuite la connexion dans VNC Viewer et entrez le mot de passe `secret`. Une nouvelle fenêtre s'ouvrira.  
Cette fenêtre donne sur le conteneur Selenium-chrome.  
Lancez enfin les tests Selenium avec la commande `. run djselenium`. Les tests seront visibles depuis la fenêtre ouverte dans VNC Viewer.  
