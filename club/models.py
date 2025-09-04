from taggit.managers import TaggableManager

from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255, blank=True, help_text="e.g. The Reds")
    founded = models.PositiveIntegerField(blank=True, null=True, help_text="Year founded")
    stadium = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    crest = models.ImageField(upload_to="clubs/crests/", blank=True, null=True)
    website = models.URLField(blank=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name
