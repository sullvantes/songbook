from taggit.managers import TaggableManager

from django.db import models


class Match(models.Model):
    home = models.ForeignKey(
        "club.Club",
        on_delete=models.CASCADE,
        related_name="home_matches",
    )
    away = models.ForeignKey(
        "club.Club",
        on_delete=models.CASCADE,
        related_name="away_matches",
    )
    kickoff = models.DateTimeField()
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ("kickoff",)

    def __str__(self):
        return f"{self.home} vs {self.away} ({self.kickoff:%Y-%m-%d %H:%M})"


class Chant(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name="chants",
    )
    song = models.ForeignKey(
        "song.Song",
        on_delete=models.CASCADE,
        related_name="chants",
    )
    minutes = models.CharField(max_length=50)

    class Meta:
        ordering = ("match", "minutes")

    def __str__(self):
        return f"{self.song} @ {self.minutes}' ({self.match})"

