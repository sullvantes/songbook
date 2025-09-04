from django.urls import path
from .views import ClubListView

app_name = "clubs"
urlpatterns = [
    path("", ClubListView.as_view(), name="list"),
]
