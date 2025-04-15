# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from typing import NamedTuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812
from selenium.webdriver.support.ui import WebDriverWait

HERE = pathlib.Path(__file__).resolve().parent
SEARCH_INPUTS = {
    "nameBox": "2016 IKWF State Championships",
    "startDateMonth": "03",
    "startDateDay": "01",
    "startDateYear": "2016",
    "endDateMonth": "03",
    "endDateDay": "31",
    "endDateYear": "2016",
}


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


def _event_search_fill_inputs(driver: webdriver.Chrome):
    base_wait = WebDriverWait(driver, 10)

    for field_id, value in SEARCH_INPUTS.items():
        input_element = base_wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )  # Wait for input to appear
        input_element.clear()  # Clear any existing text (if needed)
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


def _click_team_scores(driver: webdriver.Chrome):
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Find the 'Team Scores' element
    team_scores_span = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Team Scores']"))
    )

    # Find the grandparent element and click it
    grandparent_element = team_scores_span.find_element(By.XPATH, "./../..")
    grandparent_element.click()

    # Switch back to the main page
    driver.switch_to.default_content()


def _click_team_scores_filter(driver: webdriver.Chrome):
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Wait for the button to be clickable
    filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "pageFunc_0"))
    )

    # Click the button
    filter_button.click()

    # Switch back to the main page
    driver.switch_to.default_content()


class OptionInfo(NamedTuple):
    value: str
    text: str


def _get_division_options(driver: webdriver.Chrome) -> list[OptionInfo]:
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Wait for the <select> element to be visible
    class_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "classBox"))
    )

    # Get all <option> elements under <select id="classBox">
    options = class_box.find_elements(By.TAG_NAME, "option")

    found_options = [
        OptionInfo(value=option.get_attribute("value"), text=option.text)
        for option in options
        if option.text != ""
    ]

    # Switch back to the main page
    driver.switch_to.default_content()

    return found_options


def _capture_for_option(
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

    go_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "viewButton"))
    )
    go_button.click()

    # Locate the table element
    scores_table = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//table[contains(@class, 'tw-table')]"))
    )
    scores_table_html = scores_table.get_attribute("outerHTML")

    # Optionally, switch back to the main page (if needed)
    driver.switch_to.default_content()

    return scores_table_html


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.trackwrestling.com/")

    _main_page_click_events(driver)
    _events_page_search_events(driver)
    _event_search_fill_inputs(driver)
    _event_search_click_search(driver)
    _search_results_click_first(driver)
    _event_box_click_enter_event(driver)
    _click_team_scores(driver)
    _click_team_scores_filter(driver)
    division_options = _get_division_options(driver)

    already_open = True
    captured_html: dict[str, str] = {}
    for option_info in division_options:
        html = _capture_for_option(driver, option_info, already_open=already_open)
        if option_info.text in captured_html:
            raise RuntimeError("Invariant violation", option_info.text)

        captured_html[option_info.text] = html
        already_open = False

    with open(HERE / "team_scores.selenium.json", "w") as file_obj:
        json.dump(captured_html, file_obj, indent=2)
        file_obj.write("\n")

    driver.quit()


if __name__ == "__main__":
    main()
