from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from club.models import Club
from song.models import Song

from .forms import ChantForm, MatchForm
from .models import Match


class MatchCreateView(LoginRequiredMixin, CreateView):
    form_class = MatchForm
    template_name = "chant/add_match.html"
    success_url = reverse_lazy("home")

    def get_initial(self):
        initial = super().get_initial()
        club_slug = self.request.GET.get("club")
        if club_slug:
            club = Club.objects.filter(slug=club_slug).first()
            if club:
                initial["home"] = club.pk
        return initial

    def form_valid(self, form):
        messages.success(self.request, f"Match added: {form.instance}.")
        return super().form_valid(form)


class ChantCreateView(LoginRequiredMixin, CreateView):
    form_class = ChantForm
    template_name = "chant/add_chant.html"

    def dispatch(self, request, *args, **kwargs):
        self.match = get_object_or_404(
            Match.objects.select_related("home", "away"),
            pk=kwargs["match_pk"],
        )
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["match"] = self.match
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        song_pk = self.request.GET.get("song")
        if song_pk and str(song_pk).isdigit():
            song = Song.objects.filter(pk=song_pk, accepted=True).first()
            if song:
                initial["song"] = song.pk
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["match"] = self.match
        return context

    def form_valid(self, form):
        form.instance.match = self.match
        messages.success(
            self.request,
            f'Added "{form.instance.song}" at {form.instance.minutes}\'.',
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("songs:detail", kwargs={"pk": self.object.song_id})
