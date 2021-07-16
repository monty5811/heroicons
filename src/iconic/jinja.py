from markupsafe import Markup

import iconic


def iconic_icon(name, *, size=24, **kwargs):
    return _iconic(name, size, **kwargs)


def _iconic(name, size, **kwargs):
    svg = iconic.load_icon(name)
    start = '<svg width="{}" height="{}" '
    if kwargs:
        start += " ".join(f'{name.replace("_", "-")}="{{}}"' for name in kwargs)
        start += " "

    svg = Markup(svg.replace('<svg width="24" height="24" ', start, 1))
    return svg.format(size, size, *kwargs.values())
