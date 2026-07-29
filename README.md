# Godot Addon Manager

**This is a work in progress.**

**It does NOT have the functionality to pull dependencies yet.**

## Manifest

For an addon to make use of this, it needs a `manifest.json` file.

See [Manifest Format](MANIFEST.md) for details about declaring an addon and its
dependencies.

## CLI

Run the CLI from the repository root:

```bash
python -m cli.inspect <addon_name>
python -m cli.validate <addon_name>
```

See the [CLI documentation](cli/README.md) for more commands and details.
