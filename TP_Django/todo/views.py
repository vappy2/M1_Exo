from django.shortcuts import render
from django.http import HttpResponse

# On import notre models pour notre BDD
from .models import Task

# Il faut load notre template
from django.template import loader

#Si on utilise render 
from django.shortcuts import render, HttpResponseRedirect

def index(request):

    #On stocke nos todo dans une variable
    todolist = Task.objects.order_by('created_date')[:5]

    # Mise la mise en forme
    #output = '<br/>'.join([t.content for t in todolist])

    # On load le template qu'on veut utiliser
    template =loader.get_template('todo/index.html')

    # On renseigne l'équivalent des variables dans le template
    # Ici on n'a que la variable todolist qui est notre liste de nos todos déjà créés
    context = {
        'todolist' : todolist,
    }

    # On implémente ensuite la réponse de la page avec le template
    return HttpResponse(template.render(context, request))

    #L'autre manière de l'écrire est la suivante
    #return render(request, 'todo/indext.html', context)

def add(request) :
    #On créé notre nouveau todo
    new_todo = Task(content=request.POST['content'])
    #On le sauvegarde
    new_todo.save()
   # On fait la redirection vers l'index 
    return HttpResponseRedirect('/todo/')