from django.shortcuts import render
import requests
# Create your views here.

def exibir_card(request):
    requisicao = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?language=pt")
    dados = requisicao.json()['data']
  
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

            # Obtém a URL da imagem, garantindo que 'card_images' é uma lista e acessando o primeiro elemento
            if card.get('card_images'):  # Verifica se 'card_images' existe e não está vazia
                img_card = card['card_images'][0].get('image_url')
            else:
                img_card = 'N/A'  # Valor padrão caso não existam imagens

            contexto = {
                'id': id_card,
                'name': name,
                'typo':tipo,
                'frametype':frameType,
                'desc':desc,
                'atk':atk,
                'def':defe,
                'level':level,
                'race':race,
                'attribute':attribute,
                'img': img_card
            }
            
    

    
