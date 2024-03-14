from django.db import models


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

    class Meta:
        ordering = ["-creation_date"]


class Link(models.Model):
    class ReadStatus(models.IntegerChoices):
        READ = 1
        UNREAD = 2

    title = models.CharField(max_length=200)
    url = models.URLField()
    save_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="topic_links"
    )
    read_status = models.IntegerField(choices=ReadStatus, default=ReadStatus.UNREAD)
    note = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(
        Tag, related_name="tagged_links", blank=True, null=True
    )
    starred = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        self.title = self.title.strip().capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title[:50]

    class Meta:
        ordering = ["-save_date"]
