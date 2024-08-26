# TODO custom user creation form without the usable password thingie from 5.1 version

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user = self.set_password_and_save(user, commit=commit)
        user.email = self.cleaned_data["email"]
        if commit and hasattr(self, "save_m2m"):
            self.save_m2m()
        return user
