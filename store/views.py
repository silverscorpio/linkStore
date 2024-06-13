from django.shortcuts import render
from django.views import generic
from .models import Link, Topic, Tag


def landing(request):
    if request.user.is_authenticated:
        links = Link.objects.all()
        return render(request, "store/link_list.html", context={"link_list": links})
    return render(request, "store/landing.html")


class LinkListView(generic.ListView):
    def get_queryset(self):
        return Link.objects.order_by("save_date")


class TopicListView(generic.ListView):
    model = Topic


class TagListView(generic.ListView):
    model = Tag


class LinkDetailView(generic.DetailView):
    model = Link


class TopicDetailView(generic.DetailView):
    model = Topic


class TagDetailView(generic.DetailView):
    model = Tag
