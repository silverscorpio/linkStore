from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.landing, name="landing"),
    # list views
    path("links/", views.LinkListView.as_view(), name="links"),
    path("topics/", views.TopicListView.as_view(), name="topics"),
    path("tags/", views.TagListView.as_view(), name="tags"),
    path("links/<int:pk>/", views.LinkDetailView.as_view(), name="link-update"),
    # update
    path("links/<int:pk>/update/", views.LinkUpdateView.as_view(), name="link-update"),
    path(
        "topics/<int:pk>/update/", views.TopicUpdateView.as_view(), name="topic-update"
    ),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    # add
    path("links/add/", views.LinkCreateView.as_view(), name="link-add"),
    path("topics/add/", views.TopicCreateView.as_view(), name="topic-add"),
    path("tags/add/", views.TagCreateView.as_view(), name="tag-add"),
    # delete
    path("links/<int:pk>/delete/", views.LinkDeleteView.as_view(), name="link-delete"),
    path(
        "topics/<int:pk>/delete/", views.TopicDeleteView.as_view(), name="topic-delete"
    ),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),
]
