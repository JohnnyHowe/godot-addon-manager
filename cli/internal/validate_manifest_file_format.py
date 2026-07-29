"""Validate that an addon manifest file can be loaded."""

import json
from pathlib import Path

from .read_manifest import load_manifest_data
from .validate_manifest_format import validate_manifest_format


def validate_manifest_file_format(path: str | Path) -> list[str]:
    """Return file and format errors.

    This only guarantees that the file can be loaded into a Manifest. It does
    not perform semantic validation on the resulting Manifest object.
    """
    manifest_path = Path(path)

    if not manifest_path.is_file():
        return [f"manifest does not exist: {manifest_path}"]

    try:
        data = load_manifest_data(manifest_path)
    except json.JSONDecodeError as error:
        return [
            f"manifest contains invalid JSON at line {error.lineno}, "
            f"column {error.colno}"
        ]
    except OSError as error:
        return [f"manifest could not be read: {error}"]

    return validate_manifest_format(data)
