from django.urls import path
from .views import SongSuggestionCreateView, SongListView

app_name = "songs"
urlpatterns = [
    path("", SongListView.as_view(), name="list"),
    path("suggest/", SongSuggestionCreateView.as_view(), name="suggest"),
]
