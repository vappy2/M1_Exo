from django.db import models

# Create your models here.
class Task(models.Model) :
    content = models.CharField(max_length = 250)
    is_done = models.BooleanField(default=0)
    created_date = models.DateTimeField('Date de création')

    # Pour que la Task soit pluss représentatif dans le shell il est important de def la fonction __str__()
    #Cette fonction est aussi super utile pour la représentation de l'objet dans l'interface admin
    def __str__(self) :
        return self.content
