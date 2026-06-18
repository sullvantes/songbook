from taggit.managers import TaggableManager

from django.db import models
from django.utils.text import slugify


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    position = models.CharField(max_length=100, blank=True)
    years_active = models.CharField(max_length=50, blank=True, help_text="e.g. 2017–2023")
    photo = models.ImageField(upload_to="players/", blank=True, null=True)
    portrait = models.ImageField(
        upload_to="players/portraits/",
        blank=True,
        null=True,
        help_text="Stylized portrait (e.g. retro game art).",
    )

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base = slugify(self.name) or "player"
        slug = base
        counter = 2
        while Player.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base}-{counter}"
            counter += 1
        return slug
