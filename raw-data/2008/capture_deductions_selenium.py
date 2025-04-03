# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib

import pydantic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

HERE = pathlib.Path(__file__).resolve().parent
SEARCH_INPUTS = {
    "nameBox": "2008 IKWF State Championships",
    "startDateMonth": "03",
    "startDateDay": "01",
    "startDateYear": "2008",
    "endDateMonth": "03",
    "endDateDay": "31",
    "endDateYear": "2008",
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


def _click_teams_tab(driver: webdriver.Chrome):
    # Use normalize-space() to trim any extra whitespace
    teams_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Teams']"))
    )
    # NOTE: There may extra space (e.g. 'Teams ')

    # Click the link
    teams_link.click()


def _determine_page_size(driver: webdriver.Chrome, team_index: int):
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Wait until the <td align="center">{team_index}</td> is present
    td_query = f"//td[@align='center' and text()='{team_index}']"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, td_query))
    )

    # <font onclick="openTeamPointsDetail(...)" ...>
    font_elements = driver.find_elements(
        By.XPATH, "//font[contains(@onclick, 'openTeamPointsDetail')]"
    )

    # Switch back to the main page
    driver.switch_to.default_content()

    return len(font_elements)


class TeamDeduction(pydantic.BaseModel):
    team: str
    reason: str
    value: float


def _deductions_for_team(
    driver: webdriver.Chrome, team_index: int, primary_window: str
) -> list[TeamDeduction]:
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Find the row with <td align="center">{team_index}</td> in it
    td_query = f"//td[@align='center' and text()='{team_index}']"
    td_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, td_query))
    )

    # The same <tr> will have the clickable link for `team_index`
    sibling_tds = td_element.find_elements(By.XPATH, "./parent::tr/td")
    if len(sibling_tds) != 6:
        raise RuntimeError("Invariant violation")

    team_index_td = sibling_tds[0]
    if team_index_td.text.strip() != str(team_index):
        raise RuntimeError("Invariant violation", team_index_td.text)

    team_td = sibling_tds[2]
    team_name = team_td.text.strip()

    # Click the link on the **LAST** <td>
    last_td = sibling_tds[5]
    font_element = last_td.find_element(By.XPATH, "./font")
    font_element.click()

    # The link opens a new window
    (new_window,) = [
        window_handle
        for window_handle in driver.window_handles
        if window_handle != primary_window
    ]

    # Switch to the opened window for THIS team
    driver.switch_to.window(new_window)

    # <form id="theForm"> contains 3 tables
    parent_form = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "theForm"))
    )
    form_tables = parent_form.find_elements(By.TAG_NAME, "table")
    if len(form_tables) != 3:
        raise RuntimeError("Invariant violation")

    last_table = form_tables[2]

    # Check if there are no participants.
    no_participants_elements = last_table.find_elements(
        By.XPATH, ".//td[text()='There are no participants added to this team']"
    )
    no_participants = len(no_participants_elements) > 0

    # Find **ALL** <tr> on the page and throw away everything with a class that
    # is `colHdr`, `oddRow`, or `evenRow`. Also throw away the last one, which
    # should have `Total Team Points`. If any remain, they should be the last
    # ones.
    tr_elements = last_table.find_elements(By.TAG_NAME, "tr")
    kept_tr = [
        tr_element
        for tr_element in tr_elements
        if tr_element.get_attribute("class") not in ("colHdr", "oddRow", "evenRow")
    ]

    if len(kept_tr) == 0:
        if no_participants:
            deduction_trs = []
        else:
            raise RuntimeError("Invariant violation")
    else:
        last_tr = kept_tr[-1]
        if not last_tr.text.startswith("Total Team Points"):
            raise RuntimeError("Invariant violation", last_tr.text)

        deduction_trs = kept_tr[:-1]

    deductions: list[TeamDeduction] = []
    for tr_element in deduction_trs:
        td_elements = tr_element.find_elements(By.TAG_NAME, "td")
        if len(td_elements) != 2:
            raise RuntimeError("Invariant violation", tr_element.text)

        reason = td_elements[0].text
        value = float(td_elements[1].text)
        print((team_name, reason, value))
        deductions.append(TeamDeduction(team=team_name, reason=reason, value=value))

    # Close to the opened window for THIS team and switch back to the original
    driver.close()
    driver.switch_to.window(primary_window)

    # Switch back to the main page
    driver.switch_to.default_content()

    return deductions


def _teams_next_page(driver: webdriver.Chrome, team_index: int) -> bool:
    # Wait for the iframe to be available
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PageFrame"))
    )

    # Switch to the iframe
    driver.switch_to.frame(iframe)

    # Wait until the <td>{team_index}</td> is present
    td_query = f"//td[text()='{team_index}']"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, td_query))
    )

    # Check for presence of <i class="icon-arrow_r dgNext">
    arrow_icons = driver.find_elements(
        By.XPATH, "//i[contains(@class, 'icon-arrow_r') and contains(@class, 'dgNext')]"
    )
    if len(arrow_icons) == 0:
        # Switch back to the main page
        driver.switch_to.default_content()

        # NOTE: We are OK to exit because we know from loaded `<td>` that
        #       the page is done loading.
        return False

    if len(arrow_icons) > 1:
        raise RuntimeError("Invariant violation")

    # Click the element
    arrow_icon = arrow_icons[0]
    arrow_icon.click()

    # Switch back to the main page
    driver.switch_to.default_content()

    return True


class TeamDeductions(pydantic.RootModel[list[TeamDeduction]]):
    pass


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.trackwrestling.com/")

    _main_page_click_events(driver)
    _events_page_search_events(driver)
    _event_search_fill_inputs(driver)
    _event_search_click_search(driver)
    _search_results_click_first(driver)
    _event_box_click_enter_event(driver)
    _click_teams_tab(driver)
    # Track the (only) window before we spawn new windows
    (primary_window,) = driver.window_handles

    team_index = 1
    all_deductions: list[TeamDeduction] = []
    advanced_next_page = True
    for _ in range(100):
        page_team_count = _determine_page_size(driver, team_index)
        if page_team_count > 30:
            raise RuntimeError("Invariant violation")

        for j in range(page_team_count):
            deductions = _deductions_for_team(driver, team_index + j, primary_window)
            all_deductions.extend(deductions)

        advanced_next_page = _teams_next_page(driver, team_index)
        if not advanced_next_page:
            break

        team_index += page_team_count

    if advanced_next_page:
        raise RuntimeError("Did not terminate iteration")

    to_serialize = TeamDeductions(root=all_deductions)
    with open(HERE / "deductions.selenium.json", "w") as file_obj:
        file_obj.write(to_serialize.model_dump_json(indent=2))
        file_obj.write("\n")

    driver.quit()


if __name__ == "__main__":
    main()
