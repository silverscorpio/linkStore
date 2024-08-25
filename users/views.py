from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
from django.urls import reverse_lazy


def register(request):
    """Registration process for a new user"""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("store:links")

    context = {"form": form}
    return render(request, "registration/register.html", context)


class UserPasswordChangeView(PasswordChangeView):
    # TODO change in login template - remove the pwd change from there to the profile page when done
    success_url = reverse_lazy("users:password_change_done")


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    pass


class UserPasswordResetView(PasswordResetView):
    success_url = reverse_lazy("users:password_reset_done")


class UserPasswordResetDoneView(PasswordResetDoneView):
    pass


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("users:password_reset_complete")
