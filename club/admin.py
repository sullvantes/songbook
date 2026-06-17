from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Club


@admin.register(Club)
class ClubAdmin(ModelAdmin):
    list_display = ("name", "nickname", "founded", "stadium", "location")
    search_fields = ("name", "nickname", "stadium", "location")
    list_filter = ("founded",)
    ordering = ("name",)
    filter_horizontal = ("players",)

    fieldsets = (
        (None, {
            "fields": ("name", "nickname", "founded", "stadium", "location")
        }),
        ("Players", {
            "fields": ("players",)
        }),
        ("Tags", {
            "fields": ("tags",)
        }),
    )