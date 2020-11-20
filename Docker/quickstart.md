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

## Lancer hello-world

!![<'Lancement de Hello World'>](https://github.com/vappy2/M1_Exo/blob/main/Docker/img/hello-world.png)