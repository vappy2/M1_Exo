# TP Django : Créer une Todo list

## Fonctionnalité de l'application 

Cette application devra permettre de:

    - Afficher la liste des taches sur la page d’accueil
    - Ajouter des tâches dans la liste depuis la page d’accueil
    - Éditer une tache (dans une vue dédiée)
    - Dire que la tâche est réalisée (la barrer)
    - Supprimer une tâche

## La base de données 

Elle devrai avoir la strucutre suivante : 

    - id : int (clé primaire)
    - content : varchar(250)
    - is_done : boolean
    - created_date : datetime