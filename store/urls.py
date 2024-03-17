from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("store/", views.store, name="store"),
    path("topics/", views.topics, name="topics"),
    path("tags/", views.tags, name="tags"),
]
