"""CLI for validating an addon manifest."""

import argparse

from .internal.manifest_path import manifest_path
from .internal.read_manifest import read_manifest
from .internal.validate_manifest import validate_manifest
from .internal.validate_manifest_file_format import (
    validate_manifest_file_format,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate an addon's manifest.",
    )
    parser.add_argument("name", help="Name of the addon to validate.")
    args = parser.parse_args()

    path = manifest_path(args.name)
    errors = validate_manifest_file_format(path)
    if not errors:
        errors = validate_manifest(read_manifest(path))

    if errors:
        print(f"{args.name}: invalid")
        for error in errors:
            print(f"  - {error}")
        raise SystemExit(1)

    print(f"{args.name}: valid")


if __name__ == "__main__":
    main()
