from django.urls import path

from .views import ChantCommentCreateView, ChantCreateView, ChantDetailView, MatchCreateView, MatchListView

app_name = "chants"
urlpatterns = [
    path("", MatchListView.as_view(), name="list"),
    path("add/", MatchCreateView.as_view(), name="add_match"),
    path("chants/<int:pk>/comments/add/", ChantCommentCreateView.as_view(), name="add_comment"),
    path("chants/<int:pk>/", ChantDetailView.as_view(), name="detail"),
    path("<int:match_pk>/chants/add/", ChantCreateView.as_view(), name="add_chant"),
]
