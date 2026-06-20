from django.urls import path
from .views import (
    SongCommentCreateView,
    SongDeleteView,
    SongDetailView,
    SongListView,
    SongSuggestionCreateView,
)

app_name = "songs"
urlpatterns = [
    path("", SongListView.as_view(), name="list"),
    path("suggest/", SongSuggestionCreateView.as_view(), name="suggest"),
    path("<slug:slug>/comments/add/", SongCommentCreateView.as_view(), name="add_comment"),
    path("<slug:slug>/delete/", SongDeleteView.as_view(), name="delete"),
    path("<slug:slug>/", SongDetailView.as_view(), name="detail"),
]
