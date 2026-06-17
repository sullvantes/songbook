from taggit.managers import TaggableManager

from django.db import models
from django.utils.text import slugify


class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255, blank=True, help_text="e.g. The Reds")
    founded = models.PositiveIntegerField(blank=True, null=True, help_text="Year founded")
    stadium = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    crest = models.ImageField(upload_to="clubs/crests/", blank=True, null=True)
    website = models.URLField(blank=True)
    players = models.ManyToManyField("player.Player", related_name="clubs", blank=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base = slugify(self.name) or "club"
        slug = base
        counter = 2
        while Club.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base}-{counter}"
            counter += 1
        return slug
