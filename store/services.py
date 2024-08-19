import json

from django.db.models import Count, Max

from store.models import Topic, Link, Tag


def insert_init_data_into_store():
    """Get data from existing apple note to the DB (first time only)"""
    with open("store/data/parsed_data.json") as f:
        imported_data: dict = json.load(f)

    for k, v in imported_data.items():
        topic = Topic.objects.create(name=k)
        for i in v:
            _ = Link.objects.create(topic=topic, url=i)


class UserStats:
    def __init__(self, user):
        self.user: str = user

    # number of user links
    def get_num_links(self) -> int:
        return Link.objects.filter(owner=self.user).count()

    # number of user topics
    def get_num_topics(self) -> int:
        return Topic.objects.filter(owner=self.user).count()

    # number of user tags
    def get_num_tags(self) -> int:
        return Tag.objects.filter(owner=self.user).count()

    # number of read links
    def get_num_read_links(self) -> int:
        return Link.objects.filter(owner=self.user, is_read=True).count()

    # number of marked links
    def get_num_marked_links(self) -> int:
        return Link.objects.filter(owner=self.user, is_marked=True).count()

    # most popular topic (top 3) - topic with most links
    def get_topic_with_most_links(self) -> str:
        req_topics = [
            i.name.capitalize()
            for i in Topic.objects.filter(owner=self.user)
            .annotate(num_links=Count("topic_links"))
            .order_by("-num_links")[:3]
        ]
        if req_topics:
            return ", ".join(req_topics)
        return ""

    # most popular topic (top 3) - topic corresponding to link with maximum read count
    def get_topic_with_max_read_count_link(self) -> str:
        req_topics = [
            i.name.capitalize()
            for i in Topic.objects.filter(
                owner=self.user, topic_links__read_count__isnull=False
            )
            .annotate(max_read_count=Max("topic_links__read_count"))
            .order_by("-max_read_count")[:3]
        ]
        if req_topics:
            return ", ".join(req_topics)
        return ""

    # most popular/used tags (top 3) - tag with most links
    def get_tag_with_most_links(self) -> str:
        req_tags = [
            i.name.capitalize()
            for i in Tag.objects.filter(owner=self.user)
            .annotate(num_links=Count("tagged_links"))
            .order_by("-num_links")[:3]
        ]
        if req_tags:
            return ", ".join(req_tags)
        return ""
