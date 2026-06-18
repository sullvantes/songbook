from django.urls import path

from .views import ChantCreateView, MatchCreateView

app_name = "chants"
urlpatterns = [
    path("add/", MatchCreateView.as_view(), name="add_match"),
    path("<int:match_pk>/chants/add/", ChantCreateView.as_view(), name="add_chant"),
]
