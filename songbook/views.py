from django.http import HttpResponse


def health_check(_request):
    return HttpResponse("ok", content_type="text/plain")
