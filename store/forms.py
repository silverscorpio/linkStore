from django.forms import ModelForm
from .models import Link, Topic, Tag


class LinkForm(ModelForm):
    # TODO customise the widgets
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
