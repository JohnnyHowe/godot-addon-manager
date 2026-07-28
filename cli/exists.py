import argparse
from .addons_directory import addons_directory


def exists(addon_name: str) -> bool:
    """Validate a dependency definition."""
    addon_path = addons_directory() / addon_name

    if not addon_path.exists():
        return False

    manifest_path = addon_path / "manifest.json"

    if not manifest_path.exists():
        return False

    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check that an addon and its manifest.json exists.",
    )
    parser.add_argument("name")
    args = parser.parse_args()

    print(exists(args.name))


if __name__ == "__main__":
    main()
