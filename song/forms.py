from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from club.models import Club
from player.models import Player

from .models import Song

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, label="First name")
    last_name = forms.CharField(max_length=150, required=True, label="Last name")
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            css_class = "form-control"
            if self.is_bound and name in self.errors:
                css_class += " is-invalid"
            field.widget.attrs["class"] = css_class

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_active = False
        if commit:
            user.save()
        return user


class ResendActivationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound and "email" in self.errors:
            self.fields["email"].widget.attrs["class"] += " is-invalid"


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
