#Flask App

#On importe Flask 
from flask import Flask

#Pour faire des requests ont doit importer le module suivant 
#from flask import request

#On import la librairie pour charger des templates
from flask import render_template

#On créer l'instance de l'appli Flask
#Le paramètre name sert à déterminer le nom de l’application en fonction de si elle est démarrée en tant qu’application ou alors en tant que module d’une application.
#Si le paramètre name = main alors ça veut dire que l'appli est démarrée
app = Flask(__name__)

#Il s'agit d'un décorateur = défini l'URL ou un requête via ce décorateur
#Tout ce qui se trouve en dessous défini ce que l'application doit faire à cette URL que l'on défini dans la méthode route()
@app.route("/")

def index():
 return "Hello DC!"

#On definit une seconde vue about
@app.route("/Hello/<name>")

def hello(name = None) :
	return render_template('home.html', name=name)


#Ce code ainsi que ce qu’il y a en dessous permet de dire à Python que vous ferez tourner cette application 
#dès lors qu’elle n’est pas un module d’une autre application mais bien une application à part entière. 
if __name__ == '__main__':
    app.run(debug=True)