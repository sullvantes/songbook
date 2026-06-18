from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView

from club.models import Club
from song.models import Song

from .forms import ChantForm, MatchForm
from .models import Match


class MatchListView(ListView):
    model = Match
    context_object_name = "match_list"
    template_name = "chant/match_list.html"
    paginate_by = 20

    def get_queryset(self):
        queryset = (
            Match.objects.select_related("home", "away")
            .prefetch_related("tags")
            .annotate(chant_count=Count("chants", distinct=True))
            .order_by("-kickoff")
        )

        search_query = self.request.GET.get("q", "").strip()
        self.search_query = search_query or None
        if search_query:
            queryset = queryset.filter(
                Q(home__name__icontains=search_query)
                | Q(home__nickname__icontains=search_query)
                | Q(away__name__icontains=search_query)
                | Q(away__nickname__icontains=search_query)
                | Q(tags__name__icontains=search_query)
            )

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.search_query or ""
        context["pagination_query"] = (
            f"&{urlencode({'q': self.search_query})}" if self.search_query else ""
        )
        return context


class MatchCreateView(LoginRequiredMixin, CreateView):
    form_class = MatchForm
    template_name = "chant/add_match.html"
    success_url = reverse_lazy("chants:list")

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
