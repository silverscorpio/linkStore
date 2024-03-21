import json

from store.models import Topic, Link


def insert_init_data_into_store():
    """Get data from existing apple note to the DB (first time only)"""
    with open("store/data/parsed_data.json") as f:
        imported_data: dict = json.load(f)

    for k, v in imported_data.items():
        topic = Topic.objects.create(name=k)
        for i in v:
            _ = Link.objects.create(topic=topic, url=i)
