"""Locate addon manifest files."""

from pathlib import Path

from ..find_addons_directory import find_addons_directory


def manifest_path(addon_name: str) -> Path:
    """Return the expected path to an addon's manifest file."""
    return find_addons_directory() / addon_name / "manifest.json"
