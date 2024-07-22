from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("links/", views.LinkListView.as_view(), name="links"),
    path("topics/", views.TopicListView.as_view(), name="topics"),
    path("tags/", views.TagListView.as_view(), name="tags"),
    path("links/<int:pk>/", views.LinkUpdateView.as_view(), name="link-update"),
    path("topics/<int:pk>/", views.TopicUpdateView.as_view(), name="topic-update"),
    path("tags/<int:pk>/", views.TagUpdateView.as_view(), name="tag-update"),
    path("links/add/", views.LinkCreateView.as_view(), name="link-add"),
    path("topics/add/", views.TopicCreateView.as_view(), name="topic-add"),
    path("tags/add/", views.TagCreateView.as_view(), name="tag-update"),
]
