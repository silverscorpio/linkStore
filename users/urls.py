from django.urls import path, include
from .views import register, UserPasswordChangeView, UserPasswordChangeDoneView

app_name = "users"

urlpatterns = [
    path("password_change/", UserPasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        UserPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
