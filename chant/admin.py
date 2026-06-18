from unfold.admin import ModelAdmin
from django.contrib import admin

from .models import Chant, Match


class ChantInline(admin.TabularInline):
    model = Chant
    extra = 1
    fields = ("song", "minutes")
    autocomplete_fields = ("song",)


@admin.register(Match)
class MatchAdmin(ModelAdmin):
    list_display = ("home", "away", "kickoff")
    list_filter = ("kickoff", "home", "away")
    search_fields = ("home__name", "away__name")
    ordering = ("-kickoff",)
    date_hierarchy = "kickoff"
    inlines = [ChantInline]

    fieldsets = (
        (None, {
            "fields": ("home", "away", "kickoff"),
        }),
        ("Tags", {
            "fields": ("tags",),
        }),
    )


@admin.register(Chant)
class ChantAdmin(ModelAdmin):
    list_display = ("song", "match", "minutes")
    list_filter = ("match",)
    search_fields = ("song__title", "match__home__name", "match__away__name", "minutes")
    ordering = ("-match__kickoff", "minutes")
    autocomplete_fields = ("match", "song")

    fieldsets = (
        (None, {
            "fields": ("match", "song", "minutes"),
        }),
    )
