# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib

import bs4
import pydantic

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent


class Entrant(pydantic.BaseModel):
    division: bracket_utils.Division
    weight: int
    name_team: str
    bout_number: int | None


def _normalize_division(division_display: str) -> bracket_utils.Division:
    if division_display.strip() == "Novice":
        return "novice"

    if division_display.strip() == "Senior":
        return "senior"

    raise NotImplementedError(division_display)


def main():
    root = HERE.parent / "raw-data" / "2007"
    with open(root / "brackets.selenium.json") as file_obj:
        selenium_brackets = json.load(file_obj)

    entrants: list[Entrant] = []
    for bracket_key, html in selenium_brackets.items():
        division_display, weight_str = bracket_key.split(" - ")
        weight = int(weight_str)
        division = _normalize_division(division_display)

        soup = bs4.BeautifulSoup(html, features="html.parser")
        full_line_divs = soup.find_all("div", class_="full-line")
        for div in full_line_divs:
            td_parent = div.parent
            if td_parent.name != "td":
                raise RuntimeError("Invariant violation", td_parent)
            td_sibling = td_parent.find_next_sibling()
            if td_sibling.name != "td":
                raise RuntimeError("Invariant violation", td_sibling)

            bout_number_links = td_sibling.find_all("a", class_="segment-track")
            if len(bout_number_links) > 1:
                raise RuntimeError("Invariant violation", td_sibling)
            elif len(bout_number_links) == 1:
                bout_number = int(bout_number_links[0].text)
            else:
                bout_number = None

            entrants.append(
                Entrant(
                    division=division,
                    weight=weight,
                    name_team=div.text,
                    bout_number=bout_number,
                )
            )

    print(entrants)


if __name__ == "__main__":
    main()
