from django.shortcuts import render


def landing(request):
    if request.user.is_authenticated:
        return render(request, "store/home.html")
    return render(request, "store/landing.html")


def home(request):
    return render(request, "store/home.html")
