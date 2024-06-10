from django.contrib import admin
from .models import Topic, Tag, Link


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = [
        "read_count",
    ]


admin.site.register(Link, LinkAdmin)
admin.site.register(Topic)
admin.site.register(Tag)
