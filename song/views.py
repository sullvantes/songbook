# songs/views.py
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from club.models import Club
from player.models import Player

from .forms import SongSuggestionForm
from .models import Song

class SongListView(ListView):
    model = Song
    paginate_by = 20

    def get_queryset(self):
        return (
            Song.objects.filter(accepted=True)
            .prefetch_related("clubs", "tags")
            .select_related("player")
        )

class SongSuggestionCreateView(CreateView):
    form_class = SongSuggestionForm
    template_name = "song/suggest_song.html"
    success_url = reverse_lazy("songs:list")

    def get_initial(self):
        initial = super().get_initial()
        club_slug = self.request.GET.get("club")
        if club_slug:
            club = Club.objects.filter(slug=club_slug).first()
            if club:
                initial["club"] = club.pk
        player_slug = self.request.GET.get("player")
        if player_slug:
            player = Player.objects.filter(slug=player_slug).first()
            if player:
                initial["player"] = player.pk
        return initial

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.created_by = self.request.user
        return super().form_valid(form)
