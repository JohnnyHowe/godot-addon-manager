"""Read an addon manifest from disk."""

import json
from pathlib import Path

from .manifest import Dependency, Manifest


def read_manifest(path: str | Path) -> Manifest:
    """Read a JSON manifest at path into the in-memory representation."""
    with Path(path).open(encoding="utf-8") as manifest_file:
        data = json.load(manifest_file)

    dependencies = {
        name: Dependency(
            url=definition.get("url"),
            revision=definition.get("revision"),
        )
        for name, definition in data["dependencies"].items()
    }

    return Manifest(name=data["name"], dependencies=dependencies)
