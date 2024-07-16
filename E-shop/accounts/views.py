from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model() #Récupere la class des Users

def signup(request):
    if request.method == "POST":
        #Traiter le formulaire
        #Create le user
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
        password=password)
        #Connect le user
        login(request, user)
        return redirect('index') #Renvoi vers la vue index

    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        #Connecter le user
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password) #Verifie les infos
        if user:
            login(request, user) 
            #Renvoi sur la page d'accueil
            return redirect('index')
    #Sinon renvoi sur la page de login
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request) #Fait la déconnexion
    return redirect('index') #Renvoi sur index