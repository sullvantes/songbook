# songs/forms.py
from django import forms
from .models import Song


class SongSuggestionForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "lyrics", "description"]
        widgets = {
            "lyrics": forms.Textarea(attrs={"rows": 5}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }
