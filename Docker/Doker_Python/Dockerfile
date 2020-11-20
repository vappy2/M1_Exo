# On défini la base de l'image
# Attention : le "FROM" n'est utilisable qu'une seule fois dans un Dockfile
FROM python:3.7

# Pour executer des commande on utilise RUN
# Attention, il faut essayer de limiter les RUN afin de réduire la taille de notre image
RUN python -m pip install --upgrade pip

#On ajoute ensuite nos fichiers sources pour notre appli
ADD ./src/

#On ajoute le requirement.txt à la racine 
RUN python -m pip install -r requirements.txt

#On spécifie le port sur lequel on veut que notre projet soit écouter
# Par convention on utilise le 5000
EXPOSE 5000

#On ajoute la commande que doit faire l'image lorsqu'elle est lancé
CMD python app.py