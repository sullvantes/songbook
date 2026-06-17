from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count, IntegerField, OuterRef, Prefetch, Q, Subquery
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View
from taggit.models import Tag

from songbook.mixins import StaffRequiredMixin

from player.models import Player
from song.models import Song

from .models import Club


class ClubListView(ListView):
    model = Club
    paginate_by = 24

    def get_queryset(self):
        accepted_song_count = (
            Song.objects.filter(clubs=OuterRef("pk"), accepted=True)
            .values("clubs")
            .annotate(cnt=Count("pk"))
            .values("cnt")
        )
        player_count = (
            Player.objects.filter(clubs=OuterRef("pk"))
            .values("clubs")
            .annotate(cnt=Count("pk"))
            .values("cnt")
        )
        queryset = (
            Club.objects.annotate(
                song_count=Subquery(accepted_song_count, output_field=IntegerField()),
                player_count=Subquery(player_count, output_field=IntegerField()),
            )
            .prefetch_related(
                "tags",
                Prefetch("players", queryset=Player.objects.order_by("name")),
            )
            .order_by("name")
        )

        tag_slug = self.request.GET.get("tag", "").strip()
        self.active_tag_slug = tag_slug or None
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)

        search_query = self.request.GET.get("q", "").strip()
        self.search_query = search_query or None
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(nickname__icontains=search_query)
                | Q(stadium__icontains=search_query)
                | Q(location__icontains=search_query)
                | Q(tags__name__icontains=search_query)
                | Q(players__name__icontains=search_query)
            )

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_tag_slug"] = self.active_tag_slug
        context["active_tag"] = (
            Tag.objects.filter(slug=self.active_tag_slug).first()
            if self.active_tag_slug
            else None
        )
        context["search_query"] = self.search_query or ""
        club_content_type = ContentType.objects.get_for_model(Club)
        context["club_tags"] = (
            Tag.objects.filter(taggit_taggeditem_items__content_type=club_content_type)
            .distinct()
            .order_by("name")
        )
        query_params = {}
        if self.active_tag_slug:
            query_params["tag"] = self.active_tag_slug
        if self.search_query:
            query_params["q"] = self.search_query
        context["pagination_query"] = f"&{urlencode(query_params)}" if query_params else ""
        return context


class ClubDeleteView(StaffRequiredMixin, View):
    def post(self, request, slug):
        club = get_object_or_404(Club, slug=slug)
        name = club.name
        club.delete()
        messages.success(request, f'Deleted club "{name}".')
        return redirect("clubs:list")


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
