# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import datetime
import json
import os
import pathlib
import time
from collections.abc import Callable

import bs4
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
_REASON_PARENTS = ("div", "th", "tr", "thead", "table")


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


def _click_team_scores(driver: webdriver.Chrome) -> None:
    brackets_link = WebDriverWait(driver, _WAIT_TIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[.//div[contains(text(),'Team Scores')]]")
        )
    )

    brackets_link.click()


def _show_100_per_page(driver: webdriver.Chrome) -> None:
    select_elem = WebDriverWait(driver, _WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'select[wire\\:model\\.live="perPage"]')
        )
    )
    select = Select(select_elem)
    select.select_by_value("100")
    time.sleep(2.0)


def _capture_team_score_summary_links(driver: webdriver.Chrome) -> list[str]:
    anchors = driver.find_elements(
        By.XPATH, "//a[contains(@href, '/events/team_scoring/team/')]"
    )

    hrefs = [a.get_attribute("href") or "<missing>" for a in anchors]
    return hrefs


def _make_teams_next_page_ready(
    range_start: int,
) -> Callable[[webdriver.Chrome], str | None]:
    """Find the "Showing 101 to 200" text and wait for our page to load.

    <p class="text-sm text-gray-700 leading-5 mr-2">
      <span>Showing</span>
      <span class="font-medium">101</span>
      <span>to</span>
      <span class="font-medium">200</span>
    </p>
    """
    start_str = f"{range_start}"
    xpath_query = "//span[normalize-space(.)='Showing']/following-sibling::span[1]"

    def _weights_next_page_ready(driver: webdriver.Chrome) -> str | None:
        span = driver.find_element(By.XPATH, xpath_query)
        if span is None:
            return None

        text = span.text.strip()
        return text if text == start_str else None

    return _weights_next_page_ready


def _teams_click_next_page(driver: webdriver.Chrome, page_number: int) -> bool:
    range_start = 100 * page_number + 1

    buttons = driver.find_elements(By.CSS_SELECTOR, 'button[rel="next"]')

    if len(buttons) not in (0, 2):
        raise RuntimeError("Unexpected number of next buttons", len(buttons))

    next_page_exists = len(buttons) == 2
    if next_page_exists:
        button = buttons[0]
        button.click()
        predicate = _make_teams_next_page_ready(range_start)
        WebDriverWait(driver, _WAIT_TIME).until(predicate)
        time.sleep(0.5)

    return next_page_exists


class _CapturedHTML(pydantic.RootModel[dict[str, str]]):
    pass


def _capture_outer() -> None:
    filename = _HERE / "deductions.outer.selenium.json"
    if filename.exists():
        with open(filename, "rb") as file_obj:
            contents = file_obj.read()

        validated = _CapturedHTML.model_validate_json(contents)
        return validated.root

    login_info = _get_login_info()

    event = _Event(
        name="IKWF State Championships", start_date="2026-03-13", end_date="2026-03-14"
    )

    driver = _open_event(event, login_info)
    _click_team_scores(driver)
    _show_100_per_page(driver)
    time.sleep(2.0)

    links: list[str] = []
    next_page_exists = True
    # NOTE: This is a bounded `for` loop instead of a `while` loop.
    for i in range(10000):
        if not next_page_exists:
            break

        links.extend(_capture_team_score_summary_links(driver))

        # Prepare for next iteration of loop
        next_page_exists = _teams_click_next_page(driver, i)

    if next_page_exists:
        raise RuntimeError("Exited loop without terminating")

    if len(links) != len(set(links)):
        raise ValueError("Duplicate links exist")

    captured: dict[str, str] = {}
    previous_html: str | None = None
    for url in links:
        if url in captured:
            raise KeyError("Duplicate URL", url)

        driver.get(url)
        html = driver.page_source

        loop_count = 4
        for _ in range(loop_count):
            if html != previous_html:
                break

            time.sleep(5.0)
            html = driver.page_source

        if html == previous_html:
            raise ValueError("HTML did not change after sleeping", loop_count)

        captured[url] = html

        # Prepare for next iteration of loop
        previous_html = html

    driver.quit()

    with open(filename, "w") as file_obj:
        json.dump(captured, file_obj, indent=2)
        file_obj.write("\n")

    return captured


class _Deduction(_ForbidExtra):
    team: str
    reason: str
    value: float


class _Deductions(pydantic.RootModel[list[_Deduction]]):
    pass


def _get_deductions_for_team(url: str, html: str) -> list[_Deduction]:
    soup = bs4.BeautifulSoup(html, features="html.parser")

    reason_spans = [
        span
        for span in soup.find_all("span", {"wire:key": "0"})
        if span.text.strip() == "Reason"
    ]
    if len(reason_spans) == 0:
        return []

    if len(reason_spans) != 1:
        raise ValueError(
            "Unexpected number of <span>Reason</span>", url, len(reason_spans)
        )

    (reason_span,) = reason_spans

    path_to_table: list[bs4.Tag] = []
    for parent in reason_span.parents:
        path_to_table.append(parent)
        if parent.name == "table":
            break

    parent_tags = tuple(parent.name for parent in path_to_table)
    if parent_tags != _REASON_PARENTS:
        raise ValueError("Unexpected <span>Reason</span> parents", url, parent_tags)

    table = path_to_table[-1]

    matches: list[tuple[str, str]] = []
    for tr in table.find_all("tr"):
        row_entry = [td.text.strip() for td in tr.find_all("td")]
        if len(row_entry) == 0:
            continue

        if len(row_entry) != 2:
            raise ValueError("Unexpected table row", url, len(row_entry))

        matches.append(tuple(row_entry))

    if not matches:
        return []

    all_h2 = soup.find_all("h2")
    if len(all_h2) != 1:
        raise ValueError("Unexpected page structure <h2>", url, len(all_h2))

    team_name = all_h2[0].text.strip()

    return [
        _Deduction(team=team_name, reason=reason, value=value)
        for reason, value in matches
    ]


def _get_all_deductions(captured: dict[str, str]) -> list[_Deduction]:
    result: list[_Deduction] = []
    for url, html in captured.items():
        result.extend(_get_deductions_for_team(url, html))

    return result


def main() -> None:
    captured = _capture_outer()
    deductions = _get_all_deductions(captured)

    deductions_root = _Deductions(root=deductions)
    as_json = deductions_root.model_dump_json(indent=2)

    filename = _HERE / "deductions.selenium.json"
    with open(filename, "w") as file_obj:
        file_obj.write(as_json)
        file_obj.write("\n")


if __name__ == "__main__":
    main()
