from django.urls import path
from .views import PlayerDeleteView, PlayerDetailView, PlayerListView

app_name = "players"
urlpatterns = [
    path("", PlayerListView.as_view(), name="list"),
    path("<slug:slug>/delete/", PlayerDeleteView.as_view(), name="delete"),
    path("<slug:slug>/", PlayerDetailView.as_view(), name="detail"),
]