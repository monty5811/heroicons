import functools
import sys
from contextlib import closing
from zipfile import ZipFile

if sys.version_info >= (3, 7):
    from importlib.resources import open_binary
else:
    from importlib_resources import open_binary


class IconDoesNotExist(Exception):
    pass


@functools.lru_cache(maxsize=128)
def load_icon(name):
    zip_data = open_binary("iconic", "iconicicons.zip")
    with closing(zip_data), ZipFile(zip_data, "r") as zip_file:
        try:
            svg_bytes = zip_file.read(f"{name}.svg")
        except KeyError:
            raise IconDoesNotExist(f"The icon {name!r} does not exist.")

        # Inline SVG's don't need xmlns
        return svg_bytes.decode().replace(' xmlns="http://www.w3.org/2000/svg"', "", 1)
