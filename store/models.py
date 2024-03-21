from django.db import models
from store.utils import get_link_title


class Tag(models.Model):
    name = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-creation_date"]


class Topic(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.strip().capitalize()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-creation_date"]


class Link(models.Model):
    class LinkType(models.TextChoices):
        ARTICLE = "article"
        VIDEO = "video"
        IMAGE = "image"
        AUDIO = "audio"

    topic = models.ForeignKey(
        Topic, on_delete=models.PROTECT, related_name="topic_links"
    )
    title = models.CharField(max_length=200)
    url = models.URLField()
    save_date = models.DateField(auto_now_add=True)
    type = models.IntegerField(choices=LinkType, default=LinkType.ARTICLE)
    tag = models.ManyToManyField(Tag, related_name="tagged_links", blank=True)
    note = models.TextField(blank=True, null=True)
    has_been_read = models.BooleanField(default=False, blank=True)
    is_starred = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = get_link_title(self.url).strip().capitalize()
        if "youtube" in self.url:
            self.type = Link.LinkType.VIDEO
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title[:25]} ..."

    class Meta:
        ordering = ["-save_date", "has_been_read"]
