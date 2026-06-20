import os


class FlyHealthCheckMiddleware:
    """Normalize Host for Fly internal health probes on /health/."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/health/":
            fly_app = os.environ.get("FLY_APP_NAME")
            if fly_app:
                request.META["HTTP_HOST"] = f"{fly_app}.fly.dev"
            elif "HTTP_HOST" not in request.META:
                request.META["HTTP_HOST"] = "localhost"
        return self.get_response(request)
