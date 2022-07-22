from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import auth


def index(request):
    return render(request, 'lobby/index.html')


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
