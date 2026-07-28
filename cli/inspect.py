import argparse

from .addons_directory import addons_directory
from .internal.manifest import Manifest
from .internal.read_manifest import read_manifest


def format_manifest(manifest: Manifest) -> str:
    """Format a manifest for human-readable CLI output."""
    lines = [
        f"Addon: {manifest.name}",
        "Dependencies:",
    ]

    if not manifest.dependencies:
        lines.append("  None")
    else:
        for name, dependency in manifest.dependencies.items():
            lines.extend(
                [
                    f"  {name}",
                    f"    URL: {dependency.url or 'Not specified'}",
                    f"    Revision: {dependency.revision or 'Not specified'}",
                ]
            )

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect an addon's manifest.")
    parser.add_argument("name", help="Name of the addon to inspect.")
    args = parser.parse_args()

    manifest_path = addons_directory() / args.name / "manifest.json"
    print(format_manifest(read_manifest(manifest_path)))


if __name__ == "__main__":
    main()
