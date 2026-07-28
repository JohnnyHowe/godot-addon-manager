# Command-Line Tools

Run these scripts as Python modules from the `godot_addon_manager` repository
root. Module invocation ensures package-relative imports work correctly.

```bash
python -m cli.find_addons_directory
python -m cli.inspect <addon_name>
```

`find_addons_directory` prints the resolved path to the Godot project's
`addons` directory.

`inspect` prints information from the named addon's `manifest.json`. For
example:

```bash
python -m cli.inspect godot_addon_manager
```

Use `--help` with commands that accept arguments:

```bash
python -m cli.inspect --help
```
