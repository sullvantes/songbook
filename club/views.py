from django.views.generic import ListView

from .models import Club

class ClubListView(ListView):
    model = Club
