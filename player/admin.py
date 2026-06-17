from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(ModelAdmin):
    list_display = ("name", "slug", "position", "years_active", "photo")
    search_fields = ("name", "slug", "position", "years_active")
    readonly_fields = ("slug",)
    ordering = ("name",)

    fieldsets = (
        (None, {
            "fields": ("name", "position", "years_active", "photo")
        }),
        ("Clubs", {
            "fields": ("clubs",)
        }),
        ("Tags", {
            "fields": ("tags",)
        }),
    )