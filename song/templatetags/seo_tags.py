from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def absolute_uri(context, path=""):
    request = context.get("request")
    if request is None:
        return path
    return request.build_absolute_uri(path)
