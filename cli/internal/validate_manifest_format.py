"""Validate the format of raw addon manifest data."""


def validate_manifest_format(data: object) -> list[str]:
    """Return errors that would prevent conversion to a Manifest."""
    if not isinstance(data, dict):
        return ["manifest must contain a JSON object"]

    return [
        *_validate_name(data),
        *_validate_dependencies(data),
    ]


def _validate_name(data: dict[object, object]) -> list[str]:
    """Return errors for the manifest name field."""
    errors: list[str] = []

    if "name" not in data:
        errors.append("manifest name is missing")
    elif not isinstance(data["name"], str):
        errors.append("manifest name must be a string")

    return errors


def _validate_dependencies(data: dict[object, object]) -> list[str]:
    """Return errors for the manifest dependencies field."""
    if "dependencies" not in data:
        return ["manifest dependencies are missing"]

    dependencies = data["dependencies"]
    if not isinstance(dependencies, dict):
        return ["manifest dependencies must be an object"]

    errors: list[str] = []
    for name, definition in dependencies.items():
        errors.extend(_validate_dependency(name, definition))
    return errors


def _validate_dependency(name: object, definition: object) -> list[str]:
    """Return errors for one dependency definition."""
    errors: list[str] = []

    if not isinstance(name, str):
        errors.append("dependency names must be strings")

    if not isinstance(definition, dict):
        errors.append(f"dependency {name!r} must be an object")
        return errors

    for field_name in ("url", "revision"):
        value = definition.get(field_name)
        if value is not None and not isinstance(value, str):
            errors.append(
                f"dependency {name!r} {field_name} must be "
                "a string or null"
            )

    return errors
