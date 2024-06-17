from django.urls import path, include

app_name = "users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    # path("login/", LoginView),
    # path("register/", register_view, name="register"),
]
