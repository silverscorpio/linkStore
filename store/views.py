from django.shortcuts import render


def landing(request):
    if request.user.is_authenticated:
        return render(request, "store/store.html")
    return render(request, "store/landing.html")


def store(request):
    # home page (after login) is the store - shows all
    return render(request, "store/store.html")
