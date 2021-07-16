from django import template
from django.utils.html import format_html

import iconic

register = template.Library()


@register.simple_tag
def iconic_icon(name, *, size=24, **kwargs):
    return _iconic(name, size, **kwargs)


def _iconic(name, size, **kwargs):
    svg = iconic.load_icon(name)
    start = '<svg width="{}" height="{}" '
    if kwargs:
        start += " ".join(f'{name.replace("_", "-")}="{{}}"' for name in kwargs)
        start += " "

    svg = svg.replace('<svg width="24" height="24" ', start, 1)

    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    unsafe_values = [v + "" for v in kwargs.values()]

    return format_html(svg, size, size, *unsafe_values)
