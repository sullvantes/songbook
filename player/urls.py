from django.urls import path
from .views import PlayerListView

app_name = "players"
urlpatterns = [
    path("", PlayerListView.as_view(), name="list"),
]