from django.urls import path
from .views import ClubListView, ClubSongListView

app_name = "clubs"
urlpatterns = [
    path("", ClubListView.as_view(), name="list"),
    path("<slug:slug>/songs/", ClubSongListView.as_view(), name="songs"),
]
