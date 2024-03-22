from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("links/", views.links, name="links"),
    path("topics/", views.topics, name="topics"),
    path("tags/", views.tags, name="tags"),
]
