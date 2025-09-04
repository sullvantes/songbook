# songs/views.py
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import SongSuggestionForm
from .models import Song

class SongListView(ListView):
    model = Song

    def get_queryset(self):
        return Song.objects.filter(accepted=True)

class SongSuggestionCreateView(CreateView):
    form_class = SongSuggestionForm
    template_name = "song/suggest_song.html"
    success_url = reverse_lazy("songs:list")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.created_by = self.request.user
        return super().form_valid(form)
