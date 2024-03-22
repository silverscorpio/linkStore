from django.shortcuts import render


def landing(request):
    if request.user.is_authenticated:
        return render(request, "store/links.html")
    return render(request, "store/landing.html")


def links(request):
    # home page (after login) is the store - shows all
    return render(request, "store/links.html")


def topics(request):
    return render(request, "store/topics.html")


def tags(request):
    return render(request, "store/tags.html")
