from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(ModelAdmin):
    list_display = ("name", "position", "years_active", "photo")
    search_fields = ("name", "position", "years_active", "photo")
    ordering = ("name",)

    fieldsets = (
        (None, {
            "fields": ("name", "position", "years_active", "photo")
        }),
        ("Tags", {
            "fields": ("tags",)
        }),
    )