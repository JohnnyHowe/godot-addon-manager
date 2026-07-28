# Godot Addon Manager

Godot addons in this project use a `manifest.json` file to declare their name
and which other addons they depend on. Addons are installed directly in the
Godot project's `addons` folder.

## Format

```json
{
    "name": "example_addon",
    "dependencies": {
        "dependency_name": {
            "url": "https://example.com/dependency.git",
            "revision": "main"
        }
    }
}
```

### `name`

The addon's directory name within the Godot project's `addons` folder.

### `dependencies`

An object containing the addon's dependencies, keyed by addon name. Addons
without dependencies use an empty object:

```json
{
    "name": "example_addon",
    "dependencies": {}
}
```

Each dependency may specify:

- `url`: The URL of the dependency's source repository.
- `revision`: The source revision to install.

Unknown values may be `null`.

Dependency entries do not contain an installation path. All addons are assumed
to be installed directly in the Godot project's `addons` folder.
