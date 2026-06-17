from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Club = apps.get_model("club", "Club")
    used = set()
    for club in Club.objects.order_by("pk"):
        base = slugify(club.name) or "club"
        slug = base
        counter = 2
        while slug in used:
            slug = f"{base}-{counter}"
            counter += 1
        used.add(slug)
        club.slug = slug
        club.save(update_fields=["slug"])


class Migration(migrations.Migration):
    dependencies = [
        ("club", "0002_club_players"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="slug",
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="club",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
