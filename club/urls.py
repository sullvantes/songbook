from django.urls import path
from .views import ClubDeleteView, ClubListView, ClubSongListView

app_name = "clubs"
urlpatterns = [
    path("", ClubListView.as_view(), name="list"),
    path("<slug:slug>/delete/", ClubDeleteView.as_view(), name="delete"),
    path("<slug:slug>/songs/", ClubSongListView.as_view(), name="songs"),
]
