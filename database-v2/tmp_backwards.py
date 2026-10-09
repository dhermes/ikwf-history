import pathlib

import bracket_utils

_HERE = pathlib.Path(__file__).resolve().parent
_ALPHABET = frozenset("0123568abcdefghijklmnopqrstuvwxyz-")


def _slugify(name_normalized: str) -> str:
    simpler = name_normalized.strip().lower()
    simpler = simpler.replace('"', "")
    simpler = simpler.replace(",", "")
    simpler = simpler.replace(".", "")
    simpler = simpler.replace("'", "")
    simpler = simpler.replace("(", "")
    simpler = simpler.replace(")", "")
    simpler = simpler.replace("/", "")
    simpler = simpler.replace("&", "")
    simpler = simpler.replace("#", "")
    simpler = simpler.replace("`", "")

    slug = "-".join(simpler.split())
    if set(slug) <= _ALPHABET:
        return slug

    raise ValueError("Unexpected characters", slug, name_normalized)


def _combine_on_slug(
    slug: str,
    names_normalized: list[str],
    verified_teams: list[bracket_utils.VerifiedTeam],
) -> list[bracket_utils.VerifiedTeam]:
    name_normalized = names_normalized[0]
    combined_team = bracket_utils.VerifiedTeam(
        name_normalized=name_normalized, url_path_slug=slug, duplicates=[]
    )

    keep: list[bracket_utils.VerifiedTeam] = [combined_team]
    for verified_team in verified_teams:
        if verified_team.name_normalized not in names_normalized:
            keep.append(verified_team)
            continue

        if verified_team.url_path_slug is not None:
            raise NotImplementedError

        combined_team.duplicates.extend(verified_team.duplicates)

    updated_team_duplicates = bracket_utils.TeamDuplicates(root=keep)
    updated_team_duplicates.sort()

    return updated_team_duplicates.root


def main1() -> None:
    with open(_HERE / "_team-name-duplicates.json") as file_obj:
        as_json = file_obj.read()

    team_duplicates = bracket_utils.TeamDuplicates.model_validate_json(as_json)
    verified_teams = team_duplicates.root

    known_slugs: set[str] = set()
    for verified_team in verified_teams:
        slug = verified_team.url_path_slug
        if slug is not None:
            known_slugs.add(slug)

    new_slugs: dict[str, list[str]] = {}
    for verified_team in verified_teams:
        slug = verified_team.url_path_slug
        if slug is not None:
            continue

        # Slugify everything that does not have a slug
        new_slug = _slugify(verified_team.name_normalized)
        if new_slug in known_slugs:
            raise NotImplementedError(new_slug, verified_team.name_normalized)

        new_slugs.setdefault(new_slug, [])
        new_slugs[new_slug].append(verified_team.name_normalized)

    for new_slug, names_normalized in new_slugs.items():
        # If multiple entries have the same slug, go for it
        if len(names_normalized) == 1:
            continue

        print(new_slug)
        for name_normalized in names_normalized:
            print(f"  {name_normalized}")

        verified_teams = _combine_on_slug(new_slug, names_normalized, verified_teams)

    updated_team_duplicates = bracket_utils.TeamDuplicates(root=verified_teams)
    as_json = updated_team_duplicates.model_dump_json(indent=2)
    with open(_HERE / "_team-name-duplicates.json", "w") as file_obj:
        file_obj.write(as_json)
        file_obj.write("\n")


def main2() -> None:
    with open(_HERE / "_team-name-duplicates.json") as file_obj:
        as_json = file_obj.read()

    team_duplicates = bracket_utils.TeamDuplicates.model_validate_json(as_json)
    verified_teams = team_duplicates.root

    known_slugs: set[str] = set()
    for verified_team in verified_teams:
        slug = verified_team.url_path_slug
        if slug is not None:
            known_slugs.add(slug)

    new_slugs: dict[str, bracket_utils.VerifiedTeam] = {}
    for verified_team in verified_teams:
        slug = verified_team.url_path_slug
        if slug is not None:
            continue

        # Slugify everything that does not have a slug
        new_slug = _slugify(verified_team.name_normalized)
        if new_slug in known_slugs:
            raise NotImplementedError(new_slug, verified_team.name_normalized)

        # Fail if somehow multiple got combined together
        if verified_team.name_normalized in new_slugs:
            raise NotImplementedError

        new_slugs[new_slug] = verified_team

    latest_tournament_id = 54  # 2026
    for new_slug, verified_team in new_slugs.items():
        has_latest_year = any(
            team_duplicate.tournament_id == latest_tournament_id
            for team_duplicate in verified_team.duplicates
        )
        if not has_latest_year:
            continue

        name_normalized = verified_team.name_normalized
        print(f"{new_slug} -> {name_normalized}")


if __name__ == "__main__":
    main2()
