from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register_view

app_name = "users"

urlpatterns = [
    path("login/", LoginView),
    path("register/", register_view, name="register"),
]
