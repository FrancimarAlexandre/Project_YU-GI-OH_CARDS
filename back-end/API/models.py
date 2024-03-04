from django.db import models
from uuid import uuid4
# Create your models here.

class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key = True,default = uuid4,editable = False)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 50)
    email = models.EmailField()
    create_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.username

class FavoriteCard(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_card = models.IntegerField()
    create_at = models.DateField(auto_now_add = True)
    favorito = models.BooleanField(default=False)