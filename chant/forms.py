from django import forms

from club.models import Club
from song.models import Song

from .models import Chant, Match


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["home", "away", "kickoff", "tags"]
        widgets = {
            "kickoff": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        club_queryset = Club.objects.order_by("name")
        self.fields["home"].queryset = club_queryset
        self.fields["away"].queryset = club_queryset
        self.fields["home"].empty_label = "Select home club"
        self.fields["away"].empty_label = "Select away club"
        self.fields["kickoff"].input_formats = [
            "%Y-%m-%dT%H:%M",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M",
        ]
        self.fields["tags"].required = False
        self.fields["tags"].help_text = "Comma-separated tags (optional)."

        for name, field in self.fields.items():
            if name in ("home", "away"):
                css_class = "form-select"
            else:
                css_class = "form-control"
            if self.is_bound and name in self.errors:
                css_class += " is-invalid"
            field.widget.attrs["class"] = css_class

    def clean(self):
        cleaned_data = super().clean()
        home = cleaned_data.get("home")
        away = cleaned_data.get("away")
        if home and away and home == away:
            raise forms.ValidationError("Home and away clubs must be different.")
        return cleaned_data


class ChantForm(forms.ModelForm):
    class Meta:
        model = Chant
        fields = ["song", "minutes"]
        widgets = {
            "minutes": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. 12 or 45+2"},
            ),
        }

    def __init__(self, *args, match=None, **kwargs):
        self.match = match
        super().__init__(*args, **kwargs)
        queryset = self._songs_for_match(match)
        if self.instance.pk and self.instance.song_id:
            queryset = queryset | Song.objects.filter(pk=self.instance.song_id)
        self.fields["song"].queryset = queryset.distinct().order_by("title")
        self.fields["song"].empty_label = "Select a song"
        self.fields["minutes"].help_text = "When the chant was sung (e.g. 12, 45+2)."
        if match:
            self.fields["song"].help_text = (
                f"Songs linked to {match.home.name} or {match.away.name}."
            )

        for name, field in self.fields.items():
            css_class = "form-select" if name == "song" else "form-control"
            if self.is_bound and name in self.errors:
                css_class += " is-invalid"
            field.widget.attrs["class"] = css_class

    def _songs_for_match(self, match):
        if match is None:
            return Song.objects.none()
        return Song.objects.filter(
            accepted=True,
            clubs__in=[match.home_id, match.away_id],
        ).distinct()

    def clean_song(self):
        song = self.cleaned_data.get("song")
        if song and self.match:
            club_ids = {self.match.home_id, self.match.away_id}
            if not song.clubs.filter(pk__in=club_ids).exists():
                raise forms.ValidationError(
                    "Select a song linked to one of the clubs in this match."
                )
        return song
