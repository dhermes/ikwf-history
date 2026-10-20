import functools
import pathlib

import pydantic

_HERE = pathlib.Path(__file__).resolve().parent


class _DictStrStr(pydantic.RootModel[dict[str, str]]):
    pass


@functools.cache
def _short_name_replace() -> dict[str, str]:
    with open(_HERE / "_short-names.json", "rb") as file_obj:
        as_json = file_obj.read()

    as_root = _DictStrStr.model_validate_json(as_json)
    return as_root.root


@functools.cache
def _long_name_replace() -> dict[str, str]:
    with open(_HERE / "_long-names.json", "rb") as file_obj:
        as_json = file_obj.read()

    as_root = _DictStrStr.model_validate_json(as_json)
    return as_root.root


@functools.cache
def _first_name_replace() -> dict[str, str]:
    with open(_HERE / "_first-name-replace.json", "rb") as file_obj:
        as_json = file_obj.read()

    as_root = _DictStrStr.model_validate_json(as_json)
    return as_root.root


def _normalize_first_name(first_name: str) -> str:
    replace_map = _first_name_replace()
    return replace_map[first_name]


def normalize_competitor_name(name: str) -> str:
    parts = name.split()
    if len(parts) < 2:
        replace_map = _short_name_replace()
        return replace_map[name]

    if len(parts) > 2:
        replace_map = _long_name_replace()
        return replace_map[name]

    parts[0] = _normalize_first_name(parts[0])
    return " ".join(parts)
