from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Link, Topic, Tag


def landing(request):
    # TODO could use directly the links page (LinkListView) but maybe a different landing page?
    if request.user.is_authenticated:
        links = Link.objects.filter(topic__owner=request.user).order_by("save_date")
        return render(request, "store/link_list.html", context={"link_list": links})
    return render(request, "store/landing.html")


class LinkListView(generic.ListView):
    def get_queryset(self):
        return Link.objects.filter(topic__owner=self.request.user).order_by("save_date")


class TopicListView(generic.ListView):
    model = Topic


class TagListView(generic.ListView):
    model = Tag


class LinkDetailView(generic.DetailView):
    model = Link

    def get(self, request, *args, **kwargs):
        link = self.get_object()
        return render(request, "store/link_detail.html", context={"link": link})

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
