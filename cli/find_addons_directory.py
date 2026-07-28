from pathlib import Path


def find_addons_directory() -> Path:
    """Return the resolved path to the Godot project's addons directory."""
    return Path(__file__).resolve().parents[2]


def main() -> None:
    print(find_addons_directory())


if __name__ == "__main__":
    main()
