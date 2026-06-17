from taggit.managers import TaggableManager

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.CharField(max_length=100, blank=True)
    years_active = models.CharField(max_length=50, blank=True, help_text="e.g. 2017–2023")
    photo = models.ImageField(upload_to="players/", blank=True, null=True)

    tags = TaggableManager(blank=True)


    def __str__(self):
        return self.name
