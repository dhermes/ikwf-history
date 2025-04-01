# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from typing import NamedTuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

HERE = pathlib.Path(__file__).resolve().parent
SEARCH_INPUTS = {
    "nameBox": "2010 IKWF State Championships",
    "startDateMonth": "03",
    "startDateDay": "01",
    "startDateYear": "2010",
    "endDateMonth": "03",
    "endDateDay": "31",
    "endDateYear": "2010",
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


def _click_brackets_tab(driver: webdriver.Chrome):
    # Use normalize-space() to trim any extra whitespace
    brackets_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space(text())='Brackets']")
        )
    )
    # NOTE: There may extra space (e.g. 'Brackets ')

    # Click the link
    brackets_link.click()


class OptionInfo(NamedTuple):
    value: str
    label: str


def _all_weight_class_option_values(driver: webdriver.Chrome) -> list[OptionInfo]:
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Wait for the <select> element to be visible
    weight_group_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "weightGroupBox"))
    )

    # Get all <option> elements under <select id="weightGroupBox">
    options = weight_group_box.find_elements(By.TAG_NAME, "option")

    # Filter out disabled <option> elements
    enabled_options = [
        OptionInfo(
            value=option.get_attribute("value"), label=option.get_attribute("label")
        )
        for option in options
        if not option.get_attribute("disabled")
    ]

    # Optionally, switch back to the main page (if needed)
    driver.switch_to.default_content()

    return enabled_options


def _capture_for_option(driver: webdriver.Chrome, option_info: OptionInfo) -> str:
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    xpath_query = f"//option[@value='{option_info.value}']"
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_query))
    )

    option.click()

    # Wait for the bracket to finish loading
    bracket_label = option_info.label.replace(" - ", " ")
    xpath_query = f"//font[text()='{bracket_label}']"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_query))
    )

    # Locate the <div id="bracket-frame"> element inside the iframe
    bracket_frame = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bracket-frame"))
    )

    # Get the outerHTML of the <div id="bracket-frame"> element
    bracket_frame_html = bracket_frame.get_attribute("outerHTML")

    # Optionally, switch back to the main page (if needed)
    driver.switch_to.default_content()

    return bracket_frame_html


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.trackwrestling.com/")

    _main_page_click_events(driver)
    _events_page_search_events(driver)
    _event_search_fill_inputs(driver)
    _event_search_click_search(driver)
    _search_results_click_first(driver)
    _event_box_click_enter_event(driver)
    _click_brackets_tab(driver)
    weight_class_options = _all_weight_class_option_values(driver)

    captured_html: dict[str, str] = {}
    for option_info in weight_class_options:
        html = _capture_for_option(driver, option_info)
        if option_info.label in captured_html:
            raise RuntimeError("Invariant violation", option_info.label)

        captured_html[option_info.label] = html

    with open(HERE / "brackets.selenium.json", "w") as file_obj:
        json.dump(captured_html, file_obj, indent=2)
        file_obj.write("\n")

    driver.quit()


if __name__ == "__main__":
    main()
