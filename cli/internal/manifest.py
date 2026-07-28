"""In-memory representation of an addon manifest file."""

from dataclasses import dataclass, field


@dataclass
class Dependency:
    """Source information for an addon dependency."""

    url: str | None = None
    revision: str | None = None


@dataclass
class Manifest:
    """An addon's name and its declared dependencies."""

    name: str
    dependencies: dict[str, Dependency] = field(default_factory=dict)
