import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario,FavoriteCard
from .api.serializers import UsuarioSerializers,FavoritoCArdSerializers

import json
# Create your views here.

# CRUD
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):
    # POST
    if request.method == 'POST':
        new_user = request.data
        serializer = UsuarioSerializers(data = new_user)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status = status.HTTP_201_CREATED)
            
        return Response(status = status.HTTP_400_BAD_REQUEST)


# Cards
def exibir_card(request):
    requisicao = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?language=pt")
    dados = requisicao.json()['data']
    lista_cards = []  # Lista para armazenar os dados de cada card
  
    if dados:
        for card in dados:
            id_card = card.get('id')
            name = card.get('name')
            tipo = card.get('type')
            frameType = card.get('frameType', 'N/A')  # 'N/A' como valor padrão se não existir
            desc = card.get('desc')

            # Alguns cartões podem não ter esses atributos, então usamos get com um valor padrão
            atk = card.get('atk', 'N/A')
            defe = card.get('def', 'N/A')
            level = card.get('level', 'N/A')
            race = card.get('race', 'N/A')
            attribute = card.get('attribute', 'N/A')

            # Obtém a URL da imagem
            img_card = 'N/A'  # Valor padrão caso não existam imagens
            if 'card_images' in card and card['card_images']:
                img_card = card['card_images'][0].get('image_url', 'N/A')

            # condição para saber o tipo da carte e coletar os dados por tipo
            if tipo == "Spell Card" or tipo == "Trap Card":
                     # Cria um dicionário para o card atual e adiciona à lista
                    card_data = {
                        'id': id_card,
                        'name': name,
                        'type': tipo,
                        'frameType': frameType,
                        'desc': desc,
                        'img': img_card
                    }
                    lista_cards.append(card_data)
            elif tipo == "Link Monster":
                       # Cria um dicionário para o card atual e adiciona à lista
                        card_data = {
                            'id': id_card,
                            'name': name,
                            'type': tipo,
                            'frameType': frameType,
                            'desc': desc,
                            'atk': atk,
                            'race': race,
                            'attribute': attribute,
                            'img': img_card
                        }
                        lista_cards.append(card_data)
            else:
                # Cria um dicionário para o card atual e adiciona à lista
                card_data = {
                    'id': id_card,
                    'name': name,
                    'type': tipo,
                    'frameType': frameType,
                    'desc': desc,
                    'atk': atk,
                    'def': defe,
                    'level': level,
                    'race': race,
                    'attribute': attribute,
                    'img': img_card
                }
                lista_cards.append(card_data)

    # Passando a lista de cards para o template
    return render(request, 'index.html', {'cards': lista_cards[::150]})

    
