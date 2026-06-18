from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("player", "0002_player_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="portrait",
            field=models.ImageField(
                blank=True,
                help_text="Stylized portrait (e.g. retro game art).",
                null=True,
                upload_to="players/portraits/",
            ),
        ),
    ]
