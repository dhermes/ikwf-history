import datetime
import json
import os
import pathlib
import time

import pydantic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812
from selenium.webdriver.support.ui import Select, WebDriverWait

_HERE = pathlib.Path(__file__).resolve().parent
_ENV_USERNAME = "USA_BRACKETING_USERNAME"
_ENV_PASSWORD = "USA_BRACKETING_PASSWORD"
_WAIT_TIME = 3
_OPTION_ILLINOIS_VALUE = "14"
_OPTION_ILLINOIS_TEXT = "Illinois, USA"
_IGNORE_SEARCH_RESULTS = (
    "2026 USA Wrestling Kids Folkstyle National Championship",
    "2026 U17 Pan-Am Team Trials",
    "2026 USA Wrestling 16U & Junior Folkstyle National Championship",
    "2026 U17 Pan-Am Team Trials",
)


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid", populate_by_name=True)


class _LoginInfo(_ForbidExtra):
    username: str
    password: str


def _require_env(name: str) -> str:
    value = os.environ.get(name)
    if value is None:
        raise RuntimeError("Missing required environment variable", name)
    return value


def _get_login_info() -> _LoginInfo:
    username = _require_env(_ENV_USERNAME)
    password = _require_env(_ENV_PASSWORD)
    return _LoginInfo(username=username, password=password)


class _Event(_ForbidExtra):
    name: str
    start_date: datetime.date | None
    end_date: datetime.date


def _login_website(driver: webdriver.Chrome, login_info: _LoginInfo) -> None:
    # wait until the `login` input is present and visible
    login_input = WebDriverWait(driver, _WAIT_TIME).until(
        EC.visibility_of_element_located((By.ID, "login"))
    )
    # clear any existing text and type the username
    login_input.clear()
    time.sleep(0.05)
    login_input.send_keys(login_info.username)

    # wait until the `password` input is present and visible
    password_input = WebDriverWait(driver, _WAIT_TIME).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    # clear any existing text and type the username
    password_input.clear()
    time.sleep(0.05)
    password_input.send_keys(login_info.password)
    time.sleep(0.05)

    # Click the log in button
    login_button = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log in']"))
    )

    login_button.click()


def _go_to_events(driver: webdriver.Chrome) -> None:
    # Wait until login completes (URL changes off the login page)
    WebDriverWait(driver, _WAIT_TIME).until(EC.url_contains("usabracketing.com"))

    # Now go where you want
    driver.get("https://www.usabracketing.com/events")


def _click_search_events(driver: webdriver.Chrome) -> None:
    xpath_query = "//button[@type='button' and normalize-space()='Search Events']"
    open_search_button = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH, xpath_query))
    )

    open_search_button.click()


def _fill_out_event_search(driver: webdriver.Chrome, event: _Event) -> None:
    end_date = event.end_date
    start_date = event.start_date or end_date
    end_date_str = end_date.strftime("%m/%d/%Y")
    start_date_str = start_date.strftime("%m/%d/%Y")

    # Input: "Event Name"
    event_name = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, "event_name"))
    )

    event_name.clear()
    time.sleep(0.05)
    event_name.send_keys(event.name)
    time.sleep(0.05)

    # Input: "State"
    state_select_outer = WebDriverWait(driver, _WAIT_TIME).until(
        EC.presence_of_element_located((By.ID, "event_state_ids"))
    )
    state_select = Select(state_select_outer)
    state_select.deselect_all()
    state_select.select_by_value(_OPTION_ILLINOIS_VALUE)

    xpath_query = "//select[@id='event_state_ids']/option[@value='14']"
    select_option = driver.find_element(By.XPATH, xpath_query)
    select_option_text = select_option.text
    if select_option_text != _OPTION_ILLINOIS_TEXT:
        raise RuntimeError("Unexpected option value", select_option_text)

    # Input: "Event Dates"
    date_type_select_outer = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, "date_type"))
    )
    date_type_select = Select(date_type_select_outer)
    date_type_select.select_by_value("all")

    # Input: "Start Date"
    start_date_input = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, "event_start_date"))
    )
    start_date_input.clear()
    time.sleep(0.05)
    start_date_input.send_keys(start_date_str)
    time.sleep(0.05)

    # Input: "End Date"
    end_date_input = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, "event_end_date"))
    )
    end_date_input.clear()
    time.sleep(0.05)
    end_date_input.send_keys(end_date_str)
    time.sleep(0.05)


def _click_search_events_in_form(driver: webdriver.Chrome) -> None:
    xpath_query = "//button[@type='submit' and normalize-space()='Search Events']"
    search_button = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH, xpath_query))
    )

    search_button.click()


def _search_results_click_first(driver: webdriver.Chrome, name: str) -> str:
    table_body = WebDriverWait(driver, _WAIT_TIME).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.events tbody"))
    )
    all_trs = table_body.find_elements(By.TAG_NAME, "tr")

    tr = None
    if len(all_trs) != 1:
        kept_trs = []
        for tr in all_trs:
            html = tr.get_attribute("outerHTML")
            ignored = any(
                ignore_search_result in html
                for ignore_search_result in _IGNORE_SEARCH_RESULTS
            )
            if not ignored:
                kept_trs.append(tr)

        all_trs = kept_trs

    if len(all_trs) == 1:
        tr = all_trs[0]

    if tr is None:
        raise ValueError(f"Expected exactly 1 <tr>, found {len(all_trs)}", name)

    event_name_td = tr.find_element(By.CSS_SELECTOR, "td:nth-child(2) a.basic_link")
    event_name = event_name_td.text

    clickable_cell = tr.find_element(By.CSS_SELECTOR, "td.clickable")
    clickable_cell.click()

    return event_name


def _open_event(event: _Event, login_info: _LoginInfo) -> webdriver.Chrome:
    driver = webdriver.Chrome()
    driver.get("https://www.usabracketing.com/login")

    _login_website(driver, login_info)
    _go_to_events(driver)
    _click_search_events(driver)
    _fill_out_event_search(driver, event)
    _click_search_events_in_form(driver)
    time.sleep(0.5)
    event_name = _search_results_click_first(driver, event.name)
    if event_name != event.name:
        raise RuntimeError(
            "Tournament name does not agree with name on USA Bracketing",
            event.name,
            event_name,
        )

    return driver


def _click_brackets(driver: webdriver.Chrome) -> None:
    brackets_link = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[.//div[contains(text(),'Brackets')]]")
        )
    )

    brackets_link.click()


def _get_brackets_list(driver: webdriver.Chrome) -> list[str]:
    # e.g. https://www.usabracketing.com/events/{EVENT_ID}/brackets
    base_url = driver.current_url
    _, last_part = base_url.rsplit("/", 1)
    if last_part != "brackets":
        raise RuntimeError("Unexpected URL", base_url)

    links = driver.find_elements(By.CSS_SELECTOR, f'a[href^="{base_url}/"]')
    hrefs = [link.get_attribute("href") for link in links]
    return hrefs


def _get_bracket_html(driver: webdriver.Chrome, url: str) -> str:
    driver.get(url)

    # NOTE: The bracket name is in a unique element of the form
    #       <span class="font-gotham antialiased text-xl text-usa-red font-extrabold">
    WebDriverWait(driver, _WAIT_TIME).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "span.font-gotham.antialiased.text-xl.text-usa-red.font-extrabold",
            )
        )
    )

    html = driver.page_source
    return html


def main() -> None:
    login_info = _get_login_info()

    event = _Event(
        name="IKWF State Championships", start_date="2026-03-13", end_date="2026-03-14"
    )

    driver = _open_event(event, login_info)
    _click_brackets(driver)
    bracket_hrefs = _get_brackets_list(driver)

    captured: dict[str, str] = {}
    for bracket_href in bracket_hrefs:
        if bracket_href in captured:
            raise RuntimeError("Duplicate URL", bracket_href)
        html = _get_bracket_html(driver, bracket_href)
        captured[bracket_href] = html

    driver.quit()

    with open(_HERE / "brackets.selenium.json", "w") as file_obj:
        json.dump(captured, file_obj, indent=2)
        file_obj.write("\n")


if __name__ == "__main__":
    main()
