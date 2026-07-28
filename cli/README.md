# Command-Line Tools

Run these scripts as Python modules from the `godot_addon_manager` repository
root. Module invocation ensures package-relative imports work correctly.

```bash
python -m cli.addons_directory
python -m cli.exists <addon_name>
```

`addons_directory` prints the resolved path to the Godot project's `addons`
directory.

`exists` prints `True` when the named addon directory contains a
`manifest.json`; otherwise, it prints `False`. For example:

```bash
python -m cli.exists godot_addon_manager
```

Use `--help` with commands that accept arguments:

```bash
python -m cli.exists --help
```
