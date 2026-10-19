import json
import pathlib

_HERE = pathlib.Path(__file__).resolve().parent
_SEEN: dict[str, str] = {}


def _normalize_first_name(first_name: str) -> str:
    _SEEN[first_name] = first_name
    with open(_HERE / "seen.json", "w") as file_obj:
        json.dump(_SEEN, file_obj, indent=2, sort_keys=True)
        file_obj.write("\n")

    return first_name


def normalize_competitor_name(name: str) -> str:
    parts = name.split()
    if len(parts) > 1:
        parts[0] = _normalize_first_name(parts[0])
    return " ".join(parts)
