from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Song, MediaLink


class MediaLinkInline(admin.TabularInline):
    model = MediaLink
    extra = 1  # how many empty forms to show by default
    fields = ("media_type", "url")  # which fields to display


@admin.register(Song)
class SongAdmin(ModelAdmin):
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