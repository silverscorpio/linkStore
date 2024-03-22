from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("links/", views.LinkListView.as_view(), name="links"),
    path("topics/", views.TopicListView.as_view(), name="topics"),
    path("tags/", views.TagListView.as_view(), name="tags"),
]
