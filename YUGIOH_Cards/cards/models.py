from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Favorito(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    id_card = models.IntegerField()

    def __str__(self):
        return f' O usuário {self.usuario} favoritol o card de id {self.id_card}'
