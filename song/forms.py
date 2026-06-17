from django import forms

from club.models import Club
from player.models import Player

from .models import Song


class SongSuggestionForm(forms.ModelForm):
    club = forms.ModelChoiceField(
        queryset=Club.objects.order_by("name"),
        required=False,
        empty_label="Select a club (optional)",
    )

    class Meta:
        model = Song
        fields = ["title", "lyrics", "description", "player"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "lyrics": forms.Textarea(attrs={"rows": 5, "class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["player"].queryset = Player.objects.order_by("name")
        self.fields["player"].required = False
        self.fields["player"].empty_label = "Select a player (optional)"
        self.fields["club"].widget.attrs.update({"class": "form-select"})
        self.fields["player"].widget.attrs.update({"class": "form-select"})

    def save(self, commit=True):
        instance = super().save(commit=False)
        club = self.cleaned_data.get("club")

        if commit:
            instance.save()
            if club:
                instance.clubs.set([club])

        return instance
