"""Read an addon manifest from disk."""

import json
from pathlib import Path
from typing import Any, cast

from .manifest import Dependency, Manifest


def load_manifest_data(path: str | Path) -> object:
    """Load and return the raw JSON value from a manifest file."""
    with Path(path).open(encoding="utf-8") as manifest_file:
        return json.load(manifest_file)


def read_manifest(path: str | Path) -> Manifest:
    """Read a JSON manifest at path into the in-memory representation."""
    data = cast(dict[str, Any], load_manifest_data(path))

    dependencies = {
        name: Dependency(
            url=definition.get("url"),
            revision=definition.get("revision"),
        )
        for name, definition in data["dependencies"].items()
    }

    return Manifest(name=data["name"], dependencies=dependencies)
