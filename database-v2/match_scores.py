# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import re

_DEFAULT_SEPARATOR = "-"
_MATCH_TIME_RE = re.compile(r"^\d:\d{2}$")
_EDGE_CASES: dict[str, str | None] = {
    "Dec 4-": None,
    "Dec :32": None,
    "Dec TIE BREAKER": None,
    "Dec AA": None,
    "M-Dec AA": None,
    "Dec A.A": None,
    "Dec A.A.": None,
    "M-Dec A.A.": None,
}


def _score_split(
    result: str, score_text: str, top_win: bool, separator: str = _DEFAULT_SEPARATOR
) -> tuple[int, int]:
    # NOTE: We ignore any "extra" parts, e.g. if a score is 10--2 instead of 10-2.
    parts = [part for part in score_text.split(separator) if part.strip()]
    if len(parts) != 2:
        raise ValueError("Not a match score", score_text, result)

    score_win_str, score_lose_str = parts
    try:
        score_win = int(score_win_str)
    except ValueError as exc:
        raise ValueError(
            "Score not an integer", score_win_str, score_text, result
        ) from exc

    try:
        score_lose = int(score_lose_str)
    except ValueError as exc:
        raise ValueError(
            "Score not an integer", score_lose_str, score_text, result
        ) from exc

    if score_win < score_lose:
        score_win, score_lose = score_lose, score_win

    if top_win:
        return score_win, score_lose

    return score_lose, score_win


def _parse_match_score(
    result: str,
    prefix: str,
    top_win: bool,
    separator: str = _DEFAULT_SEPARATOR,
    strip_suffixes: tuple[str, ...] = (),
) -> tuple[int, int]:
    without_prefix = result[len(prefix) :]
    # NOTE: Order matters in `strip_suffixes`! So if one suffix is contained
    #       in another, it should come later.
    for strip_suffix in strip_suffixes:
        if without_prefix.endswith(strip_suffix):
            without_prefix = without_prefix[: -len(strip_suffix)]

    return _score_split(result, without_prefix, top_win, separator=separator)


def _maybe_parse_match_score(
    result: str, prefix: str, top_win: bool
) -> tuple[int, int] | None:
    without_prefix = result[len(prefix) :]
    if _DEFAULT_SEPARATOR not in without_prefix:
        return None

    return _parse_match_score(result, prefix, top_win)


def _handle_tech_fall(
    result: str, prefix: str, top_win: bool
) -> tuple[int, int] | None:
    without_prefix = result[len(prefix) :]
    if _DEFAULT_SEPARATOR not in without_prefix:
        return None

    if ";" in without_prefix:
        parts = without_prefix.split(";")
        if len(parts) != 2:
            raise NotImplementedError(result)
        if _MATCH_TIME_RE.match(parts[0]) is None:
            raise ValueError("Unexpected 1st part in Tech Fall", result)
        return _score_split(result, parts[1], top_win)

    if "," in without_prefix:
        parts = without_prefix.split(",")
        if len(parts) != 2:
            raise NotImplementedError(result)
        if _MATCH_TIME_RE.match(parts[0]) is None:
            raise ValueError("Unexpected 1st part in Tech Fall", result)
        return _score_split(result, parts[1], top_win)

    if without_prefix.count(":") == 2:
        parts = without_prefix.rsplit(":", 1)
        if _MATCH_TIME_RE.match(parts[0]) is None:
            raise ValueError("Unexpected 1st part in Tech Fall", result)
        return _score_split(result, parts[1], top_win)

    parts = without_prefix.split()
    if len(parts) > 2:
        raise NotImplementedError(result)

    if len(parts) == 2 and _MATCH_TIME_RE.match(parts[1]) is None:
        raise ValueError("Unexpected 2nd part in Tech Fall", result)

    return _score_split(result, parts[0], top_win)


def parse_scores(result: str, top_win: bool | None) -> tuple[int, int] | None:
    if top_win is None:
        raise NotImplementedError(result, top_win)

    if result in _EDGE_CASES:
        score_text = _EDGE_CASES[result]
        if score_text is None:
            return None

        return _score_split(result, score_text, top_win)

    # No result (2020, CANCELLED)

    if result == "":
        return None

    # Bye

    if result == "Bye":
        return None

    # Walkover

    if result.endswith("PD"):
        return None

    if result == "P-Dec" or result.startswith("P-Dec "):
        return None

    # Decision

    if result == "Dec":
        return None

    if result.startswith("Dec DOT"):
        return _parse_match_score(result, "Dec DOT", top_win)

    if result.startswith("Dec OT"):
        return _parse_match_score(result, "Dec OT", top_win)

    if result.startswith("Dec "):
        separator = _DEFAULT_SEPARATOR
        if ":" in result:
            separator = ":"
        return _parse_match_score(
            result,
            "Dec ",
            top_win,
            separator=separator,
            strip_suffixes=("DOT", "TB", " 2OT", "OT"),
        )

    # Major

    if result.startswith("Maj "):
        return _parse_match_score(result, "Maj ", top_win)

    if result.startswith("MajDec "):
        return _parse_match_score(result, "MajDec ", top_win)

    if result.startswith("M-Dec "):
        return _parse_match_score(result, "M-Dec ", top_win)

    # Tech Fall

    if result == "T-Fall":
        return None

    if result.startswith("TF "):
        return _parse_match_score(result, "TF ", top_win)

    if result.startswith("T-Fall TF"):
        return _maybe_parse_match_score(result, "T-Fall TF", top_win)

    if result.startswith("T-Fall "):
        return _handle_tech_fall(result, "T-Fall ", top_win)

    # Fall

    if result == "Fall" or result.startswith("Fall "):
        return None

    if "(Fall)" in result:
        return None

    # Unspecified overtime

    if result.startswith("OT "):
        return _parse_match_score(result, "OT ", top_win)

    if result.startswith("2-OT "):
        return _parse_match_score(result, "2-OT ", top_win)

    if result.startswith("TB-1 "):
        return _parse_match_score(result, "TB-1 ", top_win)

    if result.startswith("SV-1 "):
        return _parse_match_score(result, "SV-1 ", top_win)

    if result.startswith("SV-2 "):
        return _parse_match_score(result, "SV-2 ", top_win)

    if result.startswith("UTB "):
        return _parse_match_score(result, "UTB ", top_win)

    # Forfeit, Disqualification, etc.

    if result == "Dflt" or result.startswith("Dflt "):
        return None

    if result == "Dq" or result.startswith("Dq "):
        return None

    if result == "DQ":
        return None

    if result in ("Forf", "Forf FORFEIT", "Forf FF", "FF"):
        return None

    if result == "MFF" or result == "MFFL" or result.startswith("Inj. "):
        return None

    if result == "NC" or result == "OTHR1":
        return None

    raise NotImplementedError(result)
