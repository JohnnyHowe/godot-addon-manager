# Command-Line Tools

## Usage

Run these scripts as Python modules from the `godot_addon_manager` repository
root. Module invocation ensures package-relative imports work correctly.

```bash
python -m cli.find_addons_directory
python -m cli.inspect <addon_name>
python -m cli.validate <addon_name>
```

`find_addons_directory` prints the resolved path to the Godot project's
`addons` directory.

`inspect` prints information from the named addon's `manifest.json`. For
example:

```bash
python -m cli.inspect godot_addon_manager
```

`validate` checks the named addon's manifest format and data.

Use `--help` with commands that accept arguments:

```bash
python -m cli.inspect --help
```

## Commands

### [find_addons_directory.py](find_addons_directory.py)

```text
na
```

### [inspect.py](inspect.py)

```text
usage: python -m cli.inspect [-h] name

Inspect an addon's manifest.

positional arguments:
  name        Name of the addon to inspect.

options:
  -h, --help  show this help message and exit
```

### [validate.py](validate.py)

```text
usage: python -m cli.validate [-h] name

Validate an addon's manifest.

positional arguments:
  name        Name of the addon to validate.

options:
  -h, --help  show this help message and exit
```
