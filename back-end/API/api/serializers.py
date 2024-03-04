from rest_framework import serializers
from API import models
class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = "__all__"

class FavoritoCArdSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteCard
        fields = "__all__"   