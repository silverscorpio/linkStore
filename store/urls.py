from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("admin/store/link/", views.store, name="links"),
    path("admin/store/topic/", views.topics, name="topics"),
    path("admin/store/tag/", views.tags, name="tags"),
]
