from django.shortcuts import render
from django.views import generic
from .models import Link, Topic, Tag


def landing(request):
    if request.user.is_authenticated:
        links = Link.objects.all()
        return render(request, "store/link_list.html", context={"link_list": links})
    return render(request, "store/landing.html")


class LinkListView(generic.ListView):
    model = Link


class TopicListView(generic.ListView):
    model = Topic


class TagListView(generic.ListView):
    model = Tag
