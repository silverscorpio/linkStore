from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    if request.user.is_authenticated:
        return render(request, "store/home.html")
    return render(request, "store/landing.html")


def home(request):
    return HttpResponse(f"Hello, {request.user.username}")
