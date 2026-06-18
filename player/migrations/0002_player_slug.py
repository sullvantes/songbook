from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Player = apps.get_model("player", "Player")
    used = set()
    for player in Player.objects.order_by("pk"):
        base = slugify(player.name) or "player"
        slug = base
        counter = 2
        while slug in used:
            slug = f"{base}-{counter}"
            counter += 1
        used.add(slug)
        player.slug = slug
        player.save(update_fields=["slug"])


class Migration(migrations.Migration):
    dependencies = [
        ("player", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="slug",
            field=models.SlugField(max_length=255, null=True, db_index=False),
        ),
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="player",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
