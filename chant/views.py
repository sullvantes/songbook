from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Prefetch, Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView

from club.models import Club
from song.forms import CommentForm
from song.models import Comment, Song

from .forms import ChantForm, MatchForm
from .models import Chant, Match

COMMENT_PREFETCH = Prefetch(
    "comments",
    queryset=Comment.objects.select_related("author"),
)


class MatchListView(ListView):
    model = Match
    context_object_name = "match_list"
    template_name = "chant/match_list.html"
    paginate_by = 20
    list_period = "upcoming"

    def get_queryset(self):
        now = timezone.now()
        queryset = (
            Match.objects.select_related("home", "away")
            .prefetch_related("tags")
            .annotate(chant_count=Count("chants", distinct=True))
        )
        if self.list_period == "upcoming":
            queryset = queryset.filter(kickoff__gte=now).order_by("kickoff")
        else:
            queryset = queryset.filter(kickoff__lt=now).order_by("-kickoff")

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
        context["list_period"] = self.list_period
        context["allow_add_chant"] = self.list_period == "past"
        context["search_query"] = self.search_query or ""
        context["pagination_query"] = (
            f"&{urlencode({'q': self.search_query})}" if self.search_query else ""
        )
        return context


class UpcomingMatchListView(MatchListView):
    list_period = "upcoming"


class PastMatchListView(MatchListView):
    list_period = "past"


class MatchDetailView(DetailView):
    model = Match
    context_object_name = "match"
    template_name = "chant/match_detail.html"

    def get_queryset(self):
        return (
            Match.objects.select_related("home", "away")
            .prefetch_related(
                "tags",
                Prefetch(
                    "chants",
                    queryset=Chant.objects.filter(song__accepted=True)
                    .select_related("song")
                    .order_by("minutes"),
                ),
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_past = self.object.kickoff < timezone.now()
        context["is_past"] = is_past
        context["allow_add_chant"] = is_past and self.request.user.is_authenticated
        context["list_period"] = "past" if is_past else "upcoming"
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
        if self.match.kickoff >= timezone.now():
            messages.error(
                request,
                "Chants can only be added after a match has kicked off.",
            )
            return redirect("chants:past")
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["match"] = self.match
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        song_pk = self.request.GET.get("song")
        if song_pk and str(song_pk).isdigit():
            song = (
                Song.objects.filter(
                    pk=song_pk,
                    accepted=True,
                    clubs__in=[self.match.home_id, self.match.away_id],
                )
                .distinct()
                .first()
            )
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
        return reverse("chants:match_detail", kwargs={"pk": self.match.pk})


class ChantDetailView(DetailView):
    model = Chant
    context_object_name = "chant"
    template_name = "chant/chant_detail.html"

    def get_queryset(self):
        return (
            Chant.objects.filter(song__accepted=True)
            .select_related(
                "match",
                "match__home",
                "match__away",
                "song",
            )
            .prefetch_related(COMMENT_PREFETCH)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["is_past_match"] = self.object.match.kickoff < timezone.now()
        return context


class ChantCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        self.chant = get_object_or_404(
            Chant.objects.filter(song__accepted=True).select_related("song"),
            pk=kwargs["pk"],
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.chant = self.chant
        form.instance.author = self.request.user
        messages.success(self.request, "Comment posted.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("chants:detail", kwargs={"pk": self.chant.pk}) + "#comments"

    def form_invalid(self, form):
        for errors in form.errors.values():
            for error in errors:
                messages.error(self.request, error)
        return redirect(self.get_success_url())
