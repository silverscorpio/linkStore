from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Link, Topic, Tag
from .forms import TopicForm


def landing(request):
    # TODO could use directly the links page (LinkListView) but maybe a different landing page?
    if request.user.is_authenticated:
        links = Link.objects.filter(topic__owner=request.user).order_by("-saved_on")
        return render(request, "store/link_list.html", context={"link_list": links})
    return render(request, "store/landing.html")


class LinkListView(generic.ListView):
    def get_queryset(self):
        return Link.objects.filter(topic__owner=self.request.user).order_by("-saved_on")


class TopicListView(generic.ListView):
    def get_queryset(self):
        return Topic.objects.filter(owner=self.request.user).order_by("-updated_on")


class TagListView(generic.ListView):
    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user).order_by("-updated_on")


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


class TopicUpdateView(generic.edit.UpdateView):
    model = Topic
    form_class = TopicForm

    # TODO maybe abstract the nav bar part into base and remove separate base detail and base list
    template_name = "store/topic_detail.html"
    # context object name refers to the model data inside the context object
    # the form object inside the context object is called 'form'
    context_object_name = "topic_detail"


class TagDetailView(generic.DetailView):
    model = Tag
