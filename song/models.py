from taggit.managers import TaggableManager

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Song(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    lyrics = models.TextField(blank=True, help_text="Suggested Lyrics")
    is_fan_chant = models.BooleanField(default=True)  # distinguishes chants vs copyrighted songs
    description = models.TextField(blank=True, help_text="Background or story behind the song")
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    clubs = models.ManyToManyField("club.Club", related_name="songs", blank=True)
    player = models.ForeignKey(
        "player.Player",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="songs",
    )

    # relationships
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base = slugify(self.title) or "song"
        slug = base
        counter = 2
        while Song.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base}-{counter}"
            counter += 1
        return slug

    def branding_club(self):
        clubs = list(self.clubs.all())
        for club in clubs:
            if club.primary_color:
                return club
        return clubs[0] if clubs else None

# class AltLyric(models.Model):
#     song = models.ForeignKey(Song, related_name="alt_lyrics", on_delete=models.CASCADE)
#     lyrics = models.TextField(blank=True)
#     description = models.TextField(blank=True, help_text="Background or story behind the variation")
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     tags = TaggableManager(blank=True)

class MediaLink(models.Model):
    SONG_MEDIA_TYPES = [
        ("YOUTUBE", "YouTube"),
        ("SPOTIFY", "Spotify"),
        ("SOUNDCLOUD", "SoundCloud"),
        ("OTHER", "Other"),
    ]

    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="media_links")
    url = models.URLField()
    media_type = models.CharField(max_length=20, choices=SONG_MEDIA_TYPES, default="OTHER")

    def __str__(self):
        return f"{self.song.title} - {self.media_type}"
