from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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

    def post(self, request, *args, **kwargs):
        field, field_value = (
            request.POST.get("field"),
            bool(int(request.POST.get("status"))),
        )
        req_object = self.get_object()
        if field == "read":
            req_object.has_been_read = field_value
        elif field == "marked":
            req_object.is_starred = field_value
        req_object.save()

        return HttpResponseRedirect(reverse("store:links"))


class TopicDetailView(generic.DetailView):
    model = Topic


class TagDetailView(generic.DetailView):
    model = Tag
