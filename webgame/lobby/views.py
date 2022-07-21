from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import auth

def index(request):
    return render(request, 'lobby/index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user != None:
            auth.login(request, user)
            return redirect('lobby:index')
        return redirect('lobby:login')
    else:
        form = AuthenticationForm()
        return render(request, 'lobby/login.html', {'form': form})
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('lobby:index')
        return redirect('lobby:signup')
    else:
        form = UserCreationForm()
        return render(request, 'lobby/signup.html', {'form': form})
    
def logout(request):
    auth.logout(request)
    return redirect('lobby:index')