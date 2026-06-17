from django.urls import path
from .views import SongDeleteView, SongListView, SongSuggestionCreateView

app_name = "songs"
urlpatterns = [
    path("", SongListView.as_view(), name="list"),
    path("<int:pk>/delete/", SongDeleteView.as_view(), name="delete"),
    path("suggest/", SongSuggestionCreateView.as_view(), name="suggest"),
]
