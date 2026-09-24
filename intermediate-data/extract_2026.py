# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
import usabracketing

_HERE = pathlib.Path(__file__).resolve().parent
_ROOT = _HERE.parent
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    (
        "Jelena Cisneros - Diaz",
        "Beat the Streets Chicago-Midway",
    ): bracket_utils.Competitor(
        full_name="Jelena Cisneros - Diaz",
        first_name="Jelena",
        last_name="Cisneros - Diaz",
        team_full="Beat the Streets Chicago-Midway",
    ),
    ("Genevieve Del Muro", "nWo WC"): bracket_utils.Competitor(
        full_name="Genevieve Del Muro",
        first_name="Genevieve",
        last_name="Del Muro",
        team_full="nWo WC",
    ),
    ("Michael Olsick Jr", "Lemont Bears WC"): bracket_utils.Competitor(
        full_name="Michael Olsick Jr",
        first_name="Michael",
        last_name="Olsick",
        team_full="Lemont Bears WC",
    ),
    ("Anthony Capriola IV", "TCS WC"): bracket_utils.Competitor(
        full_name="Anthony Capriola IV",
        first_name="Anthony",
        last_name="Capriola",
        team_full="TCS WC",
    ),
    (
        "Jezrah Lopez Hernandez",
        "Beat the Streets Chicago-Midway",
    ): bracket_utils.Competitor(
        full_name="Jezrah Lopez Hernandez",
        first_name="Jezrah",
        last_name="Lopez Hernandez",
        team_full="Beat the Streets Chicago-Midway",
    ),
    ("Travis Hammons, Jr", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="Travis Hammons, Jr",
        first_name="Travis",
        last_name="Hammons",
        team_full="Harvey Twisters WC",
    ),
    ("Jaxon St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        full_name="Jaxon St Angelo",
        first_name="Jaxon",
        last_name="St Angelo",
        team_full="PSF Wrestling Academy",
    ),
    ("Jonathan Perez Jr.", "Dundee Highlanders WC"): bracket_utils.Competitor(
        full_name="Jonathan Perez Jr.",
        first_name="Jonathan",
        last_name="Perez",
        team_full="Dundee Highlanders WC",
    ),
    ("Jeremy Smith Jr.", "Downers Grove WC"): bracket_utils.Competitor(
        full_name="Jeremy Smith Jr.",
        first_name="Jeremy",
        last_name="Smith",
        team_full="Downers Grove WC",
    ),
    ("Camila S Rodriguez", "Beat the Streets Chicago-Midway"): bracket_utils.Competitor(
        full_name="Camila S Rodriguez",
        first_name="Camila",
        last_name="Rodriguez",
        team_full="Beat the Streets Chicago-Midway",
    ),
    ("Mary Jane Watie", "Sycamore WC"): bracket_utils.Competitor(
        full_name="Mary Jane Watie",
        first_name="Mary Jane",
        last_name="Watie",
        team_full="Sycamore WC",
    ),
    ("Aaron Jones Jr", "Springs Elite WC"): bracket_utils.Competitor(
        full_name="Aaron Jones Jr",
        first_name="Aaron",
        last_name="Jones",
        team_full="Springs Elite WC",
    ),
    ("Pedro Legend Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="Pedro Legend Rangel",
        first_name="Pedro Legend",
        last_name="Rangel",
        team_full="Storm Youth WC",
    ),
    ("James Newell III", "Springs Elite WC"): bracket_utils.Competitor(
        full_name="James Newell III",
        first_name="James",
        last_name="Newell",
        team_full="Springs Elite WC",
    ),
    ("Daquain Hubbard Jr.", "Homewood-Flossmoor RTC"): bracket_utils.Competitor(
        full_name="Daquain Hubbard Jr.",
        first_name="Daquain",
        last_name="Hubbard",
        team_full="Homewood-Flossmoor RTC",
    ),
    ("Demetrius Drayton Jr.", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="Demetrius Drayton Jr.",
        first_name="Demetrius",
        last_name="Drayton",
        team_full="Harvey Twisters WC",
    ),
    ("Brent Hills II", "Champions WC"): bracket_utils.Competitor(
        full_name="Brent Hills II",
        first_name="Brent",
        last_name="Hills",
        team_full="Champions WC",
    ),
    ("Alta Jane McQuary", "Junior Kahoks-Tribe Fellowship"): bracket_utils.Competitor(
        full_name="Alta Jane McQuary",
        first_name="Alta Jane",
        last_name="McQuary",
        team_full="Junior Kahoks-Tribe Fellowship",
    ),
    ("Avery De La Torre", "Fox Lake WC"): bracket_utils.Competitor(
        full_name="Avery De La Torre",
        first_name="Avery",
        last_name="De La Torre",
        team_full="Fox Lake WC",
    ),
    ("Aydan Del Muro", "nWo WC"): bracket_utils.Competitor(
        full_name="Aydan Del Muro",
        first_name="Aydan",
        last_name="Del Muro",
        team_full="nWo WC",
    ),
    ("Carter St Louis", "Villa Park Young Warriors WC"): bracket_utils.Competitor(
        full_name="Carter St Louis",
        first_name="Carter",
        last_name="St Louis",
        team_full="Villa Park Young Warriors WC",
    ),
    (
        "Cecilia Van Oppen",
        "East Peoria River Bandits Wrestling",
    ): bracket_utils.Competitor(
        full_name="Cecilia Van Oppen",
        first_name="Cecilia",
        last_name="Van Oppen",
        team_full="East Peoria River Bandits Wrestling",
    ),
    ("Cleotha Spearman lll", "East St. Louis WC"): bracket_utils.Competitor(
        full_name="Cleotha Spearman lll",
        first_name="Cleotha",
        last_name="Spearman",
        team_full="East St. Louis WC",
    ),
    ("Dai Zaria Christopher", "Astro WC"): bracket_utils.Competitor(
        full_name="Dai Zaria Christopher",
        first_name="Dai Zaria",
        last_name="Christopher",
        team_full="Astro WC",
    ),
    ("Darek Lee III", "Brawlers WC"): bracket_utils.Competitor(
        full_name="Darek Lee III",
        first_name="Darek",
        last_name="Lee",
        team_full="Brawlers WC",
    ),
    ("darnell Johnson jr", "Gomez Wrestling RTC"): bracket_utils.Competitor(
        full_name="darnell Johnson jr",
        first_name="Darnell",
        last_name="Johnson",
        team_full="Gomez Wrestling RTC",
    ),
    ("Dylan Rae Perkins", "Doom Wrestling"): bracket_utils.Competitor(
        full_name="Dylan Rae Perkins",
        first_name="Dylan Rae",
        last_name="Perkins",
        team_full="Doom Wrestling",
    ),
    ("George Mooney Jr.", "Red Raiders Wrestling Team"): bracket_utils.Competitor(
        full_name="George Mooney Jr.",
        first_name="George",
        last_name="Mooney",
        team_full="Red Raiders Wrestling Team",
    ),
    ("Glenn Harston III", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="Glenn Harston III",
        first_name="Glenn",
        last_name="Harston",
        team_full="Harvey Twisters WC",
    ),
    ("Jamal Davis, Jr", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="Jamal Davis, Jr",
        first_name="Jamal",
        last_name="Davis",
        team_full="Harvey Twisters WC",
    ),
    ("Jyel Dela Cruz", "Vittum Cats WC"): bracket_utils.Competitor(
        full_name="Jyel Dela Cruz",
        first_name="Jyel",
        last_name="Dela Cruz",
        team_full="Vittum Cats WC",
    ),
    ("Layla St. Clair", "Rock Island WC"): bracket_utils.Competitor(
        full_name="Layla St. Clair",
        first_name="Layla",
        last_name="St. Clair",
        team_full="Rock Island WC",
    ),
    ("Lesly De Santiago", "Harvard WC"): bracket_utils.Competitor(
        full_name="Lesly De Santiago",
        first_name="Lesly",
        last_name="De Santiago",
        team_full="Harvard WC",
    ),
    ("Luz Guerra Gonzalez", "Badger WC"): bracket_utils.Competitor(
        full_name="Luz Guerra Gonzalez",
        first_name="Luz",
        last_name="Guerra Gonzalez",
        team_full="Badger WC",
    ),
    ("Mary Jo Works", "Geneva Junior Vikings WC"): bracket_utils.Competitor(
        full_name="Mary Jo Works",
        first_name="Mary Jo",
        last_name="Works",
        team_full="Geneva Junior Vikings WC",
    ),
    ("Nicholas Anfeldt, Jr", "Wolves WC"): bracket_utils.Competitor(
        full_name="Nicholas Anfeldt, Jr",
        first_name="Nicholas",
        last_name="Anfeldt",
        team_full="Wolves WC",
    ),
    ("Pedro David Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="Pedro David Rangel",
        first_name="Pedro David",
        last_name="Rangel",
        team_full="Storm Youth WC",
    ),
    ("Rogelio Del Muro", "nWo WC"): bracket_utils.Competitor(
        full_name="Rogelio Del Muro",
        first_name="Rogelio",
        last_name="Del Muro",
        team_full="nWo WC",
    ),
    ("Shawn Marie Omeara", "Harlem Huskies WC"): bracket_utils.Competitor(
        full_name="Shawn Marie Omeara",
        first_name="Shawn Marie",
        last_name="Omeara",
        team_full="Harlem Huskies WC",
    ),
    ("Steven Griffith Jr.", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="Steven Griffith Jr.",
        first_name="Steven",
        last_name="Griffith",
        team_full="Storm Youth WC",
    ),
    ("Travis Hinton Jr", "Toss Em Up Wrestling Academy"): bracket_utils.Competitor(
        full_name="Travis Hinton Jr",
        first_name="Travis",
        last_name="Hinton",
        team_full="Toss Em Up Wrestling Academy",
    ),
    ("Tyronne Wiley Jr.", "Lionheart Intense Wrestling"): bracket_utils.Competitor(
        full_name="Tyronne Wiley Jr.",
        first_name="Tyronne",
        last_name="Wiley",
        team_full="Lionheart Intense Wrestling",
    ),
    ("Vada Jo Riley", "Antioch Predators WC"): bracket_utils.Competitor(
        full_name="Vada Jo Riley",
        first_name="Vada Jo",
        last_name="Riley",
        team_full="Antioch Predators WC",
    ),
    ("Caden St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        full_name="Caden St Angelo",
        first_name="Caden",
        last_name="St Angelo",
        team_full="PSF Wrestling Academy",
    ),
    ("Maverick Del Angel", "nWo WC"): bracket_utils.Competitor(
        full_name="Maverick Del Angel",
        first_name="Maverick",
        last_name="Del Angel",
        team_full="nWo WC",
    ),
    ("Michael Krueger, Jr.", "Demolition WC"): bracket_utils.Competitor(
        full_name="Michael Krueger, Jr.",
        first_name="Michael",
        last_name="Krueger",
        team_full="Demolition WC",
    ),
}


def main() -> None:
    rounds, abbreviations, brackets, team_scores, deductions = usabracketing.load_data(
        _ROOT, 2026
    )
    extracted_tournament = usabracketing.extract_tournament(
        rounds, abbreviations, brackets, deductions, team_scores, _NAME_EXCEPTIONS
    )

    as_json = extracted_tournament.model_dump_json(indent=2)

    path = _HERE / "extracted.2026.json"
    with open(path, "w") as file_obj:
        file_obj.write(as_json)
        file_obj.write("\n")


if __name__ == "__main__":
    main()
