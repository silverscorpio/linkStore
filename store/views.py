from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    return render(request, "store/landing.html")


def register(request):
    return HttpResponse("Gaand Mara")


def login(request):
    return HttpResponse("Lodu")


def home(request):
    if request.user.is_authenticated:
        return render(request, "store/home.html")
    return HttpResponse("Sorry, not logged in")
