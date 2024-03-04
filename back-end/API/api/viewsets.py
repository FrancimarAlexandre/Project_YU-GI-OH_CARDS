from rest_framework import viewsets
from API.api import serializers
from API import models
class UsuarioViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializers
    queryset = models.Usuario.objects.all()

class FavoriteCardViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FavoritoCArdSerializers
    queryset = models.FavoriteCard.objects.all()