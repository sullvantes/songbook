import os


def seo(request):
    site_name = "Football Chants Archive"
    return {
        "site_name": site_name,
        "default_meta_description": (
            "Explore football fan chants, songs, and matchday traditions "
            "from clubs and players around the world."
        ),
        "default_seo_title": site_name,
        "site_url": os.environ.get("SITE_URL", "").rstrip("/"),
    }
