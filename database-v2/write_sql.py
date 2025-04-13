# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

FILENAMES_BY_YEAR: dict[int, tuple[str, ...]] = {
    2000: ("extracted.2000.json",),
    2001: ("extracted.2001.json",),
    2002: ("extracted.2002.json",),
    2003: ("extracted.2003.json",),
    2004: ("extracted.2004.json",),
    2005: ("extracted.2005.json",),
    2006: ("extracted.2006.json",),
    2007: ("extracted.2007.json",),
    2008: ("extracted.2008.json",),
    2009: ("extracted.2009.json",),
    2010: ("extracted.2010.json",),
    2011: ("extracted.2011.json",),
    2012: ("extracted.2012.json",),
    2013: ("extracted.2013.json",),
    2014: ("extracted.2014.json",),
    2015: ("extracted.2015.json",),
    2016: ("extracted.2016.json",),
    2017: ("extracted.2017.json",),
    2018: ("extracted.2018.json",),
    2019: ("extracted.2019.json",),
    2020: ("extracted.2020.json",),
    2022: ("extracted.2022.json",),
    2023: ("extracted.2023.json",),
    2024: ("extracted.2024.json", "extracted.2024-intermediate.json"),
    2025: ("extracted.2025.json",),
}


def _handle_year(extracted_dir: pathlib.Path, year: int, filenames: tuple[str, ...]):
    for filename in filenames:
        with open(extracted_dir / filename) as file_obj:
            extracted = bracket_utils.ExtractedTournament.model_validate_json(
                file_obj.read()
            )

        with open(extracted_dir / filename, "w") as file_obj:
            file_obj.write(extracted.model_dump_json(indent=2))
            file_obj.write("\n")


def main():
    extracted_dir = HERE.parent / "intermediate-data"
    for year, filenames in FILENAMES_BY_YEAR.items():
        _handle_year(extracted_dir, year, filenames)


if __name__ == "__main__":
    main()
