from django.db import models
from django.conf import settings

# Create your models here.


# Solo para que yo me registre en la base de datos como el autor

class inicioAdmin(models.Model):
    Autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


