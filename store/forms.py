from django.forms import ModelForm
from .models import Link, Topic, Tag


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = [
            "topic",
            "tag",
            "title",
            "url",
            "type",
            "note",
        ]


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = [
            "name",
        ]


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = [
            "name",
        ]
