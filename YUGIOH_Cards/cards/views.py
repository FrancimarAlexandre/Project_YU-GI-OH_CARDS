from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import requests
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe')
            return redirect('registro')
        elif User.objects.filter(email=email).exists():
             messages.error(request, 'E-mail já cadastrado')
             return redirect('registro')
        else:
            # Create a new user instance and save it
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Automatically log the user in after registration (optional)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    
    return render(request, 'registration/register.html')
# Exibir as cartas
@login_required
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

                # Páginator
                cards = Paginator(lista_cards,200)
                page_num = request.GET.get('page')
                page = cards.get_page(page_num)
    # Passando a lista de cards para o template
    return render(request, 'index.html', {'cards': page})
