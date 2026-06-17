from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from song.models import Song

from .models import Club


class ClubListView(ListView):
    model = Club


class ClubSongListView(ListView):
    model = Song
    template_name = "club/club_song_list.html"
    context_object_name = "song_list"
    paginate_by = 20

    def get_queryset(self):
        self.club = get_object_or_404(Club, slug=self.kwargs["slug"])
        return (
            Song.objects.filter(clubs=self.club, accepted=True)
            .prefetch_related("clubs", "tags")
            .select_related("player")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["club"] = self.club
        return context
