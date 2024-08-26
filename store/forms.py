from django.forms import (
    ModelForm,
    TextInput,
    URLInput,
    Select,
    SelectMultiple,
    Textarea,
)
from .models import Link, Topic, Tag


class LinkForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["topic"].queryset = Topic.objects.filter(owner=self.user)
        self.fields["tag"].queryset = Tag.objects.filter(owner=self.user)

    class Meta:
        model = Link
        fields = [
            "title",
            "url",
            "type",
            "topic",
            "tag",
            "note",
        ]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control w-50 m-2",
                }
            ),
            "url": URLInput(
                attrs={
                    "class": "form-control w-50 m-2",
                }
            ),
            "type": Select(
                attrs={
                    "class": "form-select w-25 m-2",
                }
            ),
            "topic": Select(
                attrs={
                    "class": "form-select w-25 m-2",
                }
            ),
            "tag": SelectMultiple(
                attrs={
                    "class": "form-select w-25 m-2",
                }
            ),
            "note": Textarea(
                attrs={
                    "class": "form-control w-50 m-2",
                }
            ),
        }


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = [
            "name",
        ]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control w-50 m-2",
                }
            ),
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = [
            "name",
        ]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control w-50 m-2",
                }
            ),
        }
