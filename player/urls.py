from django.urls import path
from .views import PlayerDetailView, PlayerListView

app_name = "players"
urlpatterns = [
    path("", PlayerListView.as_view(), name="list"),
    path("<slug:slug>/", PlayerDetailView.as_view(), name="detail"),
]