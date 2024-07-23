from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Link, Topic, Tag
from .forms import TopicForm, TagForm, LinkForm


# TODO use a single base template for the update and create views (avoid repeating, as both use same template)
# TODO use reverse for success url


def landing(request):
    # TODO could use directly the links page (LinkListView) but maybe a different landing page?
    if request.user.is_authenticated:
        links = Link.objects.filter(topic__owner=request.user).order_by("-saved_on")
        return render(request, "store/link_list.html", context={"link_list": links})
    return render(request, "store/landing.html")


class LinkListView(ListView):
    def get_queryset(self):
        return Link.objects.filter(topic__owner=self.request.user).order_by("-saved_on")


class TopicListView(ListView):
    def get_queryset(self):
        return Topic.objects.filter(owner=self.request.user).order_by("-updated_on")


class TagListView(ListView):
    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user).order_by("-updated_on")


class LinkDetailView(DetailView):
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


class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = "/store/links/"


class TopicUpdateView(UpdateView):
    """
    context object name - the model data inside the context object
    form object inside the context object is called 'form'
    """

    model = Topic
    form_class = TopicForm
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = "/store/topics/"


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = "/store/tags/"


class LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = "/store/links/"


class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = "/store/topics/"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = "/store/tags/"
