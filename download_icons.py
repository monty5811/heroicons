#!/usr/bin/env python
"""
Download the latest iconicicons zip file and select only the icons.
"""
import argparse
import os
import sys
from io import BytesIO
from zipfile import ZIP_DEFLATED, ZipFile

import requests


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="e.g. 1.0.1")
    args = parser.parse_args(args)
    version = args.version

    zip_url = (
        f"https://github.com/Make-Lemonade/iconicicons/archive/refs/tags/{version}.zip"
    )
    response = requests.get(zip_url)
    if response.status_code != 200:
        print(f"Got status code {response.status_code} for {zip_url}", file=sys.stderr)
        return 1

    input_zip = ZipFile(BytesIO(response.content))
    input_prefix = f"iconicicons-{version}/src/"

    output_path = "src/iconic/iconicicons.zip"

    try:
        os.remove(output_path)
    except FileNotFoundError:
        pass
    with ZipFile(
        output_path, "w", compression=ZIP_DEFLATED, compresslevel=9
    ) as output_zip:
        n = 0
        for name in input_zip.namelist():
            if name.startswith(input_prefix) and name.endswith(".svg"):
                data = input_zip.read(name)
                data = data.replace(
                    b'width="24" height="24" viewBox="0 0 24 24" fill="none"',
                    b'width="24" height="24" fill="none" viewBox="0 0 24 24"'
                    + b' stroke="currentColor"',
                )
                new_name = name[len(input_prefix) :]
                output_zip.writestr(new_name, data)
                print(new_name)
                n += 1

    print(f"\n✅ Written ({n=})!")

    return 0


if __name__ == "__main__":
    exit(main())
