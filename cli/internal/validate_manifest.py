"""Validate the data in a loaded addon manifest."""

from .manifest import Manifest


def validate_manifest(manifest: Manifest) -> list[str]:
    """Return semantic validation errors for a loaded manifest."""
    return ["Data validation not implemented"]
