from django.urls import path, include
from .views import (
    register,
    UserPasswordChangeView,
    UserPasswordChangeDoneView,
    UserPasswordResetView,
    UserPasswordResetDoneView,
    UserPasswordResetConfirmView,
)

app_name = "users"

urlpatterns = [
    path("password_change/", UserPasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        UserPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        UserPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
