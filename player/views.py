from django.core.paginator import Paginator
from django.db.models import Count, IntegerField, OuterRef, Prefetch, Subquery
from django.views.generic import DetailView, ListView

from club.models import Club
from song.models import Song

from .models import Player


class PlayerListView(ListView):
    model = Player
    paginate_by = 24

    def get_queryset(self):
        accepted_song_count = (
            Song.objects.filter(player=OuterRef("pk"), accepted=True)
            .values("player")
            .annotate(cnt=Count("pk"))
            .values("cnt")
        )
        queryset = (
            Player.objects.annotate(
                song_count=Subquery(accepted_song_count, output_field=IntegerField()),
                club_count=Count("clubs", distinct=True),
            )
            .prefetch_related(
                "tags",
                Prefetch("clubs", queryset=Club.objects.order_by("name")),
            )
            .order_by("name")
        )

        club_slug = self.request.GET.get("club", "").strip()
        self.active_club_slug = club_slug or None
        if club_slug:
            queryset = queryset.filter(clubs__slug=club_slug)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_club_slug"] = self.active_club_slug
        context["active_club"] = (
            Club.objects.filter(slug=self.active_club_slug).first()
            if self.active_club_slug
            else None
        )
        context["pagination_query"] = (
            f"&club={self.active_club_slug}" if self.active_club_slug else ""
        )
        return context


class PlayerDetailView(DetailView):
    model = Player
    slug_url_kwarg = "slug"
    context_object_name = "player"
    paginate_by = 20

    def get_queryset(self):
        return Player.objects.prefetch_related(
            Prefetch("clubs", queryset=Club.objects.order_by("name")),
            "tags",
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        songs = (
            Song.objects.filter(player=self.object, accepted=True)
            .prefetch_related("clubs", "tags")
            .select_related("player")
            .order_by("title")
        )
        paginator = Paginator(songs, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        clubs = list(self.object.clubs.all())
        branding_club = next((club for club in clubs if club.primary_color), None)
        if branding_club is None and clubs:
            branding_club = clubs[0]
        context.update(
            {
                "song_list": page_obj.object_list,
                "page_obj": page_obj,
                "paginator": paginator,
                "is_paginated": page_obj.has_other_pages(),
                "pagination_query": "",
                "branding_club": branding_club,
            }
        )
        return context
