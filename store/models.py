from django.db import models
from store.utils import get_link_title
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=20)
    created_on = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name.lower()

    class Meta:
        ordering = ["-updated_on"]


class Topic(models.Model):
    name = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name.title()

    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-updated_on"]


class Link(models.Model):
    class LinkType(models.TextChoices):
        ARTICLE = "article"
        VIDEO = "video"
        IMAGE = "image"
        AUDIO = "audio"
        DOCUMENT = "document"

    topic = models.ForeignKey(
        Topic, on_delete=models.PROTECT, related_name="topic_links"
    )
    title = models.CharField(max_length=600)
    url = models.URLField(max_length=600)
    saved_on = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=LinkType, default=LinkType.ARTICLE)
    tag = models.ManyToManyField(Tag, related_name="tagged_links", blank=True)
    note = models.TextField(blank=True, null=True)
    has_been_read = models.BooleanField(default=False, blank=True)
    is_starred = models.BooleanField(default=False, blank=True)
    read_count = models.PositiveSmallIntegerField(
        default=0,
    )
    updated_on = models.DateField(auto_now=True)

    def pre_process_link_type(self) -> None:
        if "youtube" in self.url:
            self.type = Link.LinkType.VIDEO

        elif self.url.endswith(
            (
                "pdf",
                "doc",
                "ppt",
            )
        ):
            self.type = Link.LinkType.DOCUMENT

        elif self.url.endswith(
            (
                "jpg",
                "jpeg",
                "png",
                "bmp",
                "svg",
            )
        ):
            self.type = Link.LinkType.IMAGE

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = get_link_title(self.url).strip().capitalize()

        self.pre_process_link_type()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title[:50]} ..."

    class Meta:
        ordering = ["-saved_on", "has_been_read"]
