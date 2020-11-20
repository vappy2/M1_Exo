# Docker & Python

## Consignes 

### Écrire un Dockerfile contenant 

	* Une image ubuntu ou python 
	* installer *python3*, *pip3* et *vim* 
	* une installation automatique du fichier `requirements.txt` que vous écrirez à la racine de votre application. Renseignez vous sur ce fichier `requirements.txt`, que fait il, pourquoi est il utile? 
	* un repertoire app (dans lequel se trouvera votre application flask) 
	* une exposition du port de votre choix
	* pour finir le container devra lancer votre application flask sur le port de votre choix précédemment exposé.  
	* **Bonus** : déployer votre application sur le cloud gratuit [heroku](https://www.heroku.com)

### A quoi sert le fichier `requirements.txt` ?

Le fichier `requirements.txt` est un fichier où l'on va lister toutes les dépendances de notre application avec les versions utilisée au cours du projet.