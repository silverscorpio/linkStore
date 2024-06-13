from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("links/", views.LinkListView.as_view(), name="links"),
    path("topics/", views.TopicListView.as_view(), name="topics"),
    path("tags/", views.TagListView.as_view(), name="tags"),
    path("links/<int:pk>/", views.LinkDetailView.as_view(), name="link-detail"),
    path("topics/<int:pk>/", views.TopicDetailView.as_view(), name="topic-detail"),
    path("topics/<int:pk>/", views.TagDetailView.as_view(), name="tag-detail"),
]
