from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required(login_url="auth")
def index(request):
    folders = folder.objects.filter(user=request.user)
    context = {
        'folders':folders
    }
    return render(request, 'index.html',context)

def auth(request):
    if request.method == 'POST':
        if request.POST['action'] == 'login':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, password=password, username=username)

            if user is not None:
                login(request,user)
                print(request.user)
                return redirect('index')
            else:
                return redirect('auth')

    return render(request, 'auth.html')

def Logout(request):
    logout(request)
    return redirect('auth')