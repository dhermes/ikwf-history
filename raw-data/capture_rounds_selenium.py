# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import argparse
import json
import pathlib
from typing import NamedTuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

HERE = pathlib.Path(__file__).resolve().parent
_MATCH_FORMAT = (
    "[boutType] :: [boutNo] :: [wFName] [wLName] ([wTeam]) :: "
    "[lFName] [lLName] ([lTeam]) :: [scoreSummary]"
)


def _get_event_name(year: int, alternate: bool) -> str:
    if alternate:
        if year == 2024:
            return "IKWF Int/Ban State Championships"

        raise NotImplementedError(year)

    if year == 2007:
        return "2007 IKWF State Championships"

    if year == 2008:
        return "2008 IKWF State Championships"

    if year == 2009:
        return "2009 IKWF State Championships"

    if year == 2010:
        return "2010 IKWF State Championships"

    if year == 2011:
        return "2011 IKWF State Championships"

    if year == 2012:
        return "2012 IKWF State Championships"

    if year == 2013:
        return "2013 IKWF State Championships"

    if year == 2014:
        return "2014 IKWF State Championships"

    if year == 2015:
        return "2015 IKWF State Championships"

    if year == 2016:
        return "2016 IKWF State Championships"

    if year == 2017:
        return "2017 IKWF State Championships"

    if year == 2018:
        return "2018 IKWF State Championships"

    if year == 2019:
        return "2019 IKWF State Championships"

    if year == 2020:
        return "CANCELLED - 2020 IKWF State Championships"

    if year == 2022:
        return "2022 IKWF State Championships"

    if year == 2023:
        return "2023 IKWF State Championships"

    if year == 2024:
        return "IKWF Senior/Novice State Championships"

    if year == 2025:
        return "2025 IKWF State Championships"

    raise NotImplementedError(year)


def _get_year_root(root: pathlib.Path, year: int, alternate: bool) -> pathlib.Path:
    if alternate:
        if year == 2024:
            return root / "2024-intermediate"

        raise NotImplementedError(year)

    return root / str(year)


def _main_page_click_events(driver: webdriver.Chrome):
    # Wait for the element to appear
    event_span = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Events']"))
    )

    # Click the <span>Events</span>
    event_span.click()


def _events_page_search_events(driver: webdriver.Chrome):
    # Wait for the button to be clickable
    event_search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "eventSearchButton"))
    )

    # Click the button
    event_search_button.click()


def _event_search_fill_inputs(driver: webdriver.Chrome, year: int, alternate: bool):
    base_wait = WebDriverWait(driver, 10)

    event_name = _get_event_name(year, alternate)
    search_inputs = {
        "nameBox": event_name,
        "startDateMonth": "03",
        "startDateDay": "01",
        "startDateYear": str(year),
        "endDateMonth": "03",
        "endDateDay": "31",
        "endDateYear": str(year),
    }

    for field_id, value in search_inputs.items():
        input_element = base_wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )  # Wait for input to appear
        input_element.clear()  # Clear any existing text
        input_element.send_keys(value)  # Enter the value


def _event_search_click_search(driver: webdriver.Chrome):
    # Wait for the button to be clickable
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Search']"))
    )

    # Click the button
    search_button.click()


def _search_results_click_first(driver: webdriver.Chrome):
    # Wait for the anchor link to be clickable
    anchor_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "anchor_0"))
    )

    # Click the link
    anchor_link.click()


def _event_box_click_enter_event(driver: webdriver.Chrome):
    # Wait for the button to be clickable
    enter_event_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Enter Event']"))
    )

    # Click the button
    enter_event_button.click()


def _click_results_sidebar(driver: webdriver.Chrome):
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Find the 'Results' element
    team_scores_span = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Results']"))
    )

    # Find the grandparent element and click it
    grandparent_element = team_scores_span.find_element(By.XPATH, "./../..")
    grandparent_element.click()

    # Switch back to the main page
    driver.switch_to.default_content()


def _click_round_results(driver: webdriver.Chrome):
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Click <a>Round Results</a>
    round_results_anchor = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Round Results"))
    )

    # Click the link
    round_results_anchor.click()

    # Switch back to the main page
    driver.switch_to.default_content()


class OptionInfo(NamedTuple):
    value: str
    text: str


def _get_round_options(driver: webdriver.Chrome) -> list[OptionInfo]:
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Wait for the <select> element to be visible
    round_id_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "roundIdBox"))
    )

    # Get all <option> elements under <select id="roundIdBox">
    options = round_id_box.find_elements(By.TAG_NAME, "option")

    found_options = [
        OptionInfo(value=option.get_attribute("value"), text=option.text)
        for option in options
        if option.text != "All Rounds"
    ]

    # Switch back to the main page
    driver.switch_to.default_content()

    return found_options


def get_args() -> tuple[int, bool]:
    parser = argparse.ArgumentParser(prog="capture-deductions-selenium")
    parser.add_argument("--year", required=True, type=int)
    parser.add_argument("--alternate", action="store_true")
    parsed = parser.parse_args()
    return parsed.year, parsed.alternate


def _capture_for_round(
    driver: webdriver.Chrome, option_info: OptionInfo, already_open: bool
) -> str:
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    if not already_open:
        # Wait for the button to be clickable
        filter_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "pageFunc_0"))
        )

        # Click the button
        filter_button.click()

    xpath_query = f"//option[@value='{option_info.value}']"
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_query))
    )

    option.click()

    # Now set match format in "Advanced" settings
    advanced_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Advanced"))
    )
    advanced_link.click()

    # Fill out <id id="format">
    format_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "format"))
    )
    format_input.clear()
    format_input.send_keys(_MATCH_FORMAT)

    go_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Go']"))
    )
    go_button.click()

    # Locate the `<h1>` for the round
    if "'" in option_info.text:
        raise RuntimeError("Invariant violation", option_info.text)
    xpath_query = f"//h1[text()='{option_info.text}']"
    title_h1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_query))
    )

    parent_section = title_h1.find_element(By.XPATH, "./..")
    if parent_section.tag_name != "section":
        raise RuntimeError("Invariant violation", parent_section.text)

    page_content_html = parent_section.get_attribute("outerHTML")

    # Switch back to the main page (if needed)
    driver.switch_to.default_content()

    return page_content_html


def main():
    year, alternate = get_args()

    driver = webdriver.Chrome()
    driver.get("https://www.trackwrestling.com/")

    _main_page_click_events(driver)
    _events_page_search_events(driver)
    _event_search_fill_inputs(driver, year, alternate)
    _event_search_click_search(driver)
    _search_results_click_first(driver)
    _event_box_click_enter_event(driver)
    _click_results_sidebar(driver)
    _click_round_results(driver)
    round_options = _get_round_options(driver)

    already_open = True
    captured_html: dict[str, str] = {}
    for option_info in round_options:
        html = _capture_for_round(driver, option_info, already_open=already_open)
        if option_info.text in captured_html:
            raise RuntimeError("Invariant violation", option_info.text)

        captured_html[option_info.text] = html
        already_open = False

    root = _get_year_root(HERE, year, alternate)
    with open(root / "rounds.selenium.json", "w") as file_obj:
        json.dump(captured_html, file_obj, indent=2)
        file_obj.write("\n")

    driver.quit()


if __name__ == "__main__":
    main()
