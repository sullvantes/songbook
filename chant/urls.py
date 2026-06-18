from django.urls import path

from .views import ChantCreateView, MatchCreateView, MatchListView

app_name = "chants"
urlpatterns = [
    path("", MatchListView.as_view(), name="list"),
    path("add/", MatchCreateView.as_view(), name="add_match"),
    path("<int:match_pk>/chants/add/", ChantCreateView.as_view(), name="add_chant"),
]
