from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("home/", views.home, name="home"),
]
