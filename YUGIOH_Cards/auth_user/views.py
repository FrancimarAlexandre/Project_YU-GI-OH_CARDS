from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
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