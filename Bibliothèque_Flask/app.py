#Flask App

#On importe Flask 
from flask import Flask

#On import la librairie pour charger des templates
from flask import render_template

#on importe json pour pouvoir lire le fichier
import json
from flask import jsonify

#On créer l'instance de l'appli Flask

app = Flask(__name__)

#On défini les routes
@app.route("/")

def index():
	return "Welcome to my app"

#On instancie notre liste de livre
#On load notre Json
def loadJson(path):
    f = open(path)
    loadedJson = json.load(f)
    f.close()
    return loadedJson

#On utilise la fonction pour load notre JSON puis on le défini come notre variable
booklist = loadJson('data/books.json')

#On affiche les livre continue dans la liste
@app.route("/api/books", methods=['GET'])

#La fonction jsonify permemt d'afficher l'intégralité d'un fichier type json
def afficher_book() :
	return jsonify(booklist)

@app.route('/api/books/<int:book_id>', methods=['GET'])

def book_id_search(book_id):

    # On créer un tableau vide afin de stocké les résultats
    livres_trouve = []

    #On parcours notre liste
    for book in booklist:

    	# pour chaque livre qui a un id identique à celui dans l'url on l'ajoute dans notre tableau de résultat
        if book['id'] == book_id:

            livres_trouve.append(book)
            #On affiche le résultat 
            return jsonify(livres_trouve)

        else :
        	# On affiche une erreur
            return 'Aucun livre ne porte cet id'

@app.route('/api/books/<string:book_title>')

def book_title_search(book_title) :

	#On créer un tableau vide pour stocké les livres trouvés
	find_book = []

	#On parcours notre liste & pour chaque livres trouvés on l'ajoute à notre tableau vide
	for book in booklist :

		#on check les titres
		if book['title'] == book_title :

			#Si la condition est vérifié on l'add au tableau
			find_book.append(book)

			#on retourne le résult
			return jsonify(find_book)

		else :

			#On return une erreur
			return "Aucun livre ne porte ce titre"


#Exec du code
if __name__ == '__main__':
    app.run(debug=True)