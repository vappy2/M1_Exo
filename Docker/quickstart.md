# Concept de Docker 

## Comprendre la différence entre images et containers

Un **container** va être le contenant de nos besoins.
Une **image*** va être les contenus de notre contenant (= container) 

*Exemple* : Si l'on part en vacances avec une voiture avec des bagages à l'intérieur, et bien **la voiture est le container** tandis que **les différents bagages seront les différentes images**

Attention : Une image correspond à 1 bagagage, donc *x bagages = x images*

## À quoi sert un `Dockerfile` ?

Un `Dockerfile£` est la liste de ce que l'on va mettre dans notre container. Il faut cependant faire très attention à **l'ordre** dans lequel on ajoute nos images. 
Par exemple pour notre cas on va faire un `Dockerfile` dans l'ordre suivant : 

* Mettre OS donc Ubuntu
* Mettre Pyhton & Python 3
* Install pip & pip3
* Install Flask avec notre appli

## Lancement `hello-world`

`$ docker run hello-world` 

Cette commande permet de lancer le container "hello-world"

## Lancement `getting-started`

`$ docker run -d -p 80:80 docker/getting-started`

J'aurais ainsi ma page sur le localhost:80

## Les commandes `build`, `run`, `exec`

* `build` : Permet de construire une image depuis un Dockerfile et un "context".
* `run` : Permet de crée une couche de conteneur inscriptible sur l'image specifiée, puis la démarre.
* `exec` : Permet de lancer une commande dans un conteneur en cours d'éxécution.

## Le port dans un container 

### Commande pour spécifier le port 
` docker run -p numeroduport`

### Son rôle 
Lorsque que je vais lancer un serveur web, il va rendre les pages web sur le port 80, mais seulement à l’intérieur du conteneur. Je n’y aurais pas accès car c’est totalement isolé, le conteneur a son propre réseau. Afin de pouvoir accéder aux pages web, je vais utiliser l’option -p qui va me permettre de spécifier le port de ma machine et lui dire vers quel port du conteneur je veux faire la liaison. De cette façon, je vais pouvoir accéder aux pages web via mon navigateur.