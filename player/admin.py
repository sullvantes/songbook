from django import forms
from unfold.admin import ModelAdmin
from django.contrib import admin

from club.models import Club

from .models import Player


class PlayerAdminForm(forms.ModelForm):
    clubs = forms.ModelMultipleChoiceField(
        queryset=Club.objects.order_by("name"),
        required=False,
        help_text="Clubs this player is linked to.",
        widget=forms.SelectMultiple(attrs={"size": 12}),
    )

    class Meta:
        model = Player
        fields = (
            "name",
            "position",
            "years_active",
            "portrait",
            "photo",
            "tags",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["clubs"].initial = self.instance.clubs.all()

    def save(self, commit=True):
        player = super().save(commit=commit)

        def set_clubs():
            player.clubs.set(self.cleaned_data["clubs"])

        if commit:
            set_clubs()
        else:
            original_save_m2m = self.save_m2m

            def save_m2m():
                original_save_m2m()
                set_clubs()

            self.save_m2m = save_m2m

        return player


@admin.register(Player)
class PlayerAdmin(ModelAdmin):
    form = PlayerAdminForm
    list_display = ("name", "slug", "position", "years_active", "portrait", "photo")
    search_fields = ("name", "slug", "position", "years_active", "clubs__name")
    readonly_fields = ("slug",)
    ordering = ("name",)

    fieldsets = (
        (None, {
            "fields": ("name", "position", "years_active", "portrait", "photo")
        }),
        ("Clubs", {
            "fields": ("clubs",)
        }),
        ("Tags", {
            "fields": ("tags",)
        }),
    )