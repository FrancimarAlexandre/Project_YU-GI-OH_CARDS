from rest_framework import viewsets
from API.api import serializers
from API import models
class UsuarioViewset(viewsets.ModelViewSet):
    serializers_class = serializers.UsuarioSerializers
    queryset = models.Usuario.objects.all()

class FavoriteCardViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.FavoritoCArdSerializers
    queryset = models.FavoriteCard.objects.all()