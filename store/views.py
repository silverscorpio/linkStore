from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Link, Topic, Tag
from django.contrib.auth.models import User
from .forms import TopicForm, TagForm, LinkForm
from .services import UserStats


# TODO object and detail object (object exists already in context)
def landing(request):
    """Home page with login/register screen"""
    if request.user.is_authenticated:
        return redirect("store:links")
    return render(request, "store/landing.html")


def stats(request):
    if request.user.is_authenticated:
        logged_in_user = User.objects.get(id=request.user.id)
        user_stats = UserStats(user=logged_in_user)

        # note - a simple dict doesn't work, needs a key-value where value is the actual dict of context
        stat_context = {
            "stats_data": {
                "Total Links": user_stats.get_num_links(),
                "Total Topics": user_stats.get_num_topics(),
                "Total Tags": user_stats.get_num_tags(),
                "Links Read": user_stats.get_num_read_links(),
                "Links Marked": user_stats.get_num_marked_links(),
                "Topics with most number of Links (top-3)": user_stats.get_topic_with_most_links(),
                "Topics with most clicked/opened Links (top-3)": user_stats.get_topic_with_max_read_count_link(),
                "Tags with most number of Links (top-3)": user_stats.get_tag_with_most_links(),
            }
        }
        return render(
            request,
            "store/stats.html",
            stat_context,
        )
    return render(request, "store/landing.html")


class LinkListView(ListView):
    def get_queryset(self):
        return Link.objects.filter(topic__owner=self.request.user).order_by("-saved_on")


class TopicListView(ListView):
    def get_queryset(self):
        return Topic.objects.filter(owner=self.request.user).order_by("-created_on")


class TagListView(ListView):
    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user).order_by("-created_on")


class LinkDetailView(DetailView):
    model = Link

    # TODO refactor this into separate func calls in JS (decouple)
    def post(self, request, *args, **kwargs):
        field, field_value = (
            request.POST.get("field"),
            bool(int(request.POST.get("status"))),
        )
        instance: Link = self.get_object()
        if field == "read":
            instance.is_read = field_value
        elif field == "marked":
            instance.is_marked = field_value
        elif field == "read_count":
            instance: Link = self.get_object()

            # clicking/opening the url marks it as read
            instance.is_read = True
            instance.read_count += 1

        instance.save()

        return HttpResponseRedirect(reverse("store:links"))


class BaseLinkView:
    model = Link
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = reverse_lazy("store:links")


class BaseTopicView:
    """
    context object name - the model data inside the context object
    form object inside the context object is called 'form'
    """

    model = Topic
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = reverse_lazy("store:topics")


class BaseTagView:
    model = Tag
    context_object_name = "detail_object"
    extra_context = {"model_name": model.__name__}
    template_name = "store/create_update_view.html"
    success_url = reverse_lazy("store:tags")


# Link
class LinkCreateView(BaseLinkView, CreateView):
    form_class = LinkForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class LinkUpdateView(BaseLinkView, UpdateView):
    form_class = LinkForm


class LinkDeleteView(BaseLinkView, DeleteView):
    template_name = "store/delete_view.html"


# Topic
class TopicCreateView(BaseTopicView, CreateView):
    form_class = TopicForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TopicUpdateView(BaseTopicView, UpdateView):
    form_class = TopicForm


class TopicDeleteView(BaseTopicView, DeleteView):
    template_name = "store/delete_view.html"


# Tag
class TagCreateView(BaseTagView, CreateView):
    form_class = TagForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TagUpdateView(BaseTagView, UpdateView):
    form_class = TagForm


class TagDeleteView(BaseTagView, DeleteView):
    template_name = "store/delete_view.html"
