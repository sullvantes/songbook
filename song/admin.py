from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from unfold.admin import ModelAdmin

from player.models import Player

from .models import MediaLink, Song


class SongAdminForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        player_field = self.fields.get("player")
        if player_field is None:
            return

        club_ids = self._selected_club_ids()
        if club_ids:
            queryset = Player.objects.filter(clubs__in=club_ids).distinct().order_by("name")
            if self.instance.player_id:
                queryset = queryset | Player.objects.filter(pk=self.instance.player_id)
            player_field.help_text = "Only players linked to the selected clubs are shown."
        else:
            queryset = Player.objects.none()
            if self.instance.player_id:
                queryset = Player.objects.filter(pk=self.instance.player_id)
            player_field.help_text = "Select at least one club to choose a player."

        player_field.queryset = queryset.distinct().order_by("name")

    def _selected_club_ids(self):
        if self.data:
            return [int(pk) for pk in self.data.getlist("clubs") if str(pk).isdigit()]
        if self.instance.pk:
            return list(self.instance.clubs.values_list("pk", flat=True))
        return []

    def clean(self):
        cleaned_data = super().clean()
        player = cleaned_data.get("player")
        clubs = cleaned_data.get("clubs")
        if player and clubs and not player.clubs.filter(pk__in=clubs).exists():
            raise ValidationError(
                {"player": "Selected player has not played at any of the selected clubs."}
            )
        return cleaned_data


class MediaLinkInline(admin.TabularInline):
    model = MediaLink
    extra = 1  # how many empty forms to show by default
    fields = ("media_type", "url")  # which fields to display


@admin.register(Song)
class SongAdmin(ModelAdmin):
    form = SongAdminForm
    list_display = ("title", "display_clubs", "player", "is_fan_chant", "created_at", "updated_at")
    list_filter = ("is_fan_chant", "clubs", "player", "created_at")
    search_fields = ("title", "lyrics", "description", "clubs__name", "player__name")
    filter_horizontal = ("clubs",)

    inlines = [MediaLinkInline]

    fieldsets = (
        (None, {
            "fields": ("title", "lyrics", "description", "is_fan_chant")
        }),
        ("Related To", {
            "fields": ("clubs", "player")
        }),
        ("Tags", {
            "fields": ("tags",)
        }),
    )

    @admin.display(description="Clubs")
    def display_clubs(self, obj):
        return ", ".join(obj.clubs.values_list("name", flat=True))