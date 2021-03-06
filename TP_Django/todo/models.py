import datetime 

from django.db import models
from django.utils import timezone #Cet import permet d'obtenir la date selon où on se trouve dans le monde

# Create your models here.
class Task(models.Model) :
    content = models.CharField(max_length = 250)
    is_done = models.BooleanField(default = False)
    created_date = models.DateTimeField('Date de création', auto_now_add=True)

    # Pour que la Task soit pluss représentatif dans le shell il est important de def la fonction __str__()
    #Cette fonction est aussi super utile pour la représentation de l'objet dans l'interface admin
    def __str__(self) :
        return self.content
    
