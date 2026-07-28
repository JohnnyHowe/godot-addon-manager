"""Locate addon manifest files."""

from pathlib import Path

from ..find_addons_directory import find_addons_directory


def manifest_path(addon_name: str) -> Path:
    """Return the path to an addon's existing manifest file."""
    path = find_addons_directory() / addon_name / "manifest.json"

    if not path.is_file():
        raise FileNotFoundError(
            f"Addon {addon_name!r} has no manifest at {path}"
        )

    return path
