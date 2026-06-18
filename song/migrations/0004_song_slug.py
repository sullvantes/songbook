from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Song = apps.get_model("song", "Song")
    used = set()
    for song in Song.objects.order_by("pk"):
        base = slugify(song.title) or "song"
        slug = base
        counter = 2
        while slug in used:
            slug = f"{base}-{counter}"
            counter += 1
        used.add(slug)
        song.slug = slug
        song.save(update_fields=["slug"])


class Migration(migrations.Migration):
    dependencies = [
        ("song", "0003_song_clubs_m2m"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="slug",
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="song",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
