from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

from django.http import HttpResponse


def welcome(request):
    return render(request, "mainApp/welcome.html")


def about(request):
    return render(request, "mainApp/about.html")


def contact(request):
    return render(request, "mainApp/contact.html")


def features(request):
    return render(request, "mainApp/features.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, "mainApp/login.html")


def logout(request):
    auth.logout(request)
    return redirect('welcome-page')


def home(request):
    context = {
        'viewName': 'Główny dashboard'
    }
    return render(request, "mainApp/home.html", context)


def benchmarking(request):
    context = {
        'viewName': 'Porównanie uczelni'
    }
    return render(request, "mainApp/benchmarking.html", context)


def profile(request):
    context = {
        'viewName': 'Profil użytkownika'
    }
    return render(request, 'mainApp/profile.html', context)


def statistics(request):
    context = {
        'viewName': 'Statystyki uczelni'
    }
    return render(request, 'mainApp/statistics.html', context)
