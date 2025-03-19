# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "HIL": "HILLSBORO JR TOPPERS WRESTLING CLUB",
}
TEAM_NAME_MAPPING = {
    "HILLSBORO JR TOPPERS WRESTLING CLUB": 170,
}


def main():
    with open(HERE / "extracted.2004.json") as file_obj:
        extracted = json.load(file_obj)

    raise NotImplementedError(len(extracted))


if __name__ == "__main__":
    main()
