#Flask App

#On importe Flask 
from flask import Flask

#On import la librairie pour charger des templates
from flask import render_template

#On créer l'instance de l'appli Flask

app = Flask(__name__)

#On défini les routes
@app.route("/")

def index():
	return "Welcome to my app"

#On instancie notre livre
book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]

#On affiche les livre continue dans la liste
@app.route("/api/books", methods=['GET'])

def afficher_book() :
	#for i in book :
	#	print(book[i])
	print('pouet')

#Exec du code
if __name__ == '__main__':
    app.run(debug=True)