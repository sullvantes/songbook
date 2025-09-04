from song.models import Song
from club.models import Club
from player.models import Player

# app/utils.py
def dashboard_callback(request):
    return {
        "total_songs": Song.objects.count(),
        "total_clubs": Club.objects.count(),
        "total_players": Player.objects.count(),
    }
