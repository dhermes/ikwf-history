# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
import re

import bs4
import chardet

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent


def junior_iwf_1999():
    path = ROOT / "raw-data" / "iwf" / "1999" / "junior" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Wt: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "iwf" / "1999" / "junior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def novice_iwf_1999():
    path = ROOT / "raw-data" / "iwf" / "1999" / "novice" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Wt: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "iwf" / "1999" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_iwf_1999():
    path = ROOT / "raw-data" / "iwf" / "1999" / "senior" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Wt: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "iwf" / "1999" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def _iwf_2000_clean_line(line: str) -> str:
    return line.replace("\xa0", " ").rstrip()


def _iwf_2000_clean_pre(text: str) -> str:
    text = text.rstrip()
    text = text + "\n"

    for _ in range(50):
        if text.startswith("\n"):
            text = text[1:]
        else:
            break

    if text.startswith("\n"):
        raise NotImplementedError

    return text


def junior_iwf_2000():
    path = ROOT / "raw-data" / "iwf" / "2000" / "junior" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")

    match_headers = soup.find_all("h3", string=re.compile(r"^Wt: "))
    weights_pre = {}
    for i, match_header in enumerate(match_headers):
        weight_text = match_header.text
        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)

        end_h3 = None
        if i < len(match_headers) - 1:
            end_h3 = match_headers[i + 1]

        pre_between = []
        for element in match_header.next_siblings:
            if element == end_h3:
                break
            if isinstance(element, bs4.Tag) and element.name == "pre":
                pre_between.append(_iwf_2000_clean_line(element.text))

        weights_pre[weight] = _iwf_2000_clean_pre("\n".join(pre_between))

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "iwf" / "2000" / "junior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def novice_iwf_2000():
    path = ROOT / "raw-data" / "iwf" / "2000" / "novice" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")

    match_headers = soup.find_all("h3", string=re.compile(r"^Wt: "))
    weights_pre = {}
    for i, match_header in enumerate(match_headers):
        weight_text = match_header.text
        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)

        end_h3 = None
        if i < len(match_headers) - 1:
            end_h3 = match_headers[i + 1]

        pre_between = []
        for element in match_header.next_siblings:
            if element == end_h3:
                break
            if isinstance(element, bs4.Tag) and element.name == "pre":
                pre_between.append(_iwf_2000_clean_line(element.text))

        weights_pre[weight] = _iwf_2000_clean_pre("\n".join(pre_between))

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]

        if weight == 115:
            needs_newline = "\n" + " " * 70 + "K ARGUE-RW ------+"
            pre_text = pre_text.replace(needs_newline, "\n" + needs_newline)

        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "iwf" / "2000" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_iwf_2000():
    path = ROOT / "raw-data" / "iwf" / "2000" / "senior" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")

    match_headers = soup.find_all("h3", string=re.compile(r"^Wt: "))
    weights_pre = {}
    for i, match_header in enumerate(match_headers):
        weight_text = match_header.text
        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)

        end_h3 = None
        if i < len(match_headers) - 1:
            end_h3 = match_headers[i + 1]

        pre_between = []
        for element in match_header.next_siblings:
            if element == end_h3:
                break
            if isinstance(element, bs4.Tag) and element.name == "pre":
                pre_between.append(_iwf_2000_clean_line(element.text))

        weights_pre[weight] = _iwf_2000_clean_pre("\n".join(pre_between))

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "iwf" / "2000" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def novice_2000():
    path = ROOT / "raw-data" / "2000" / "novice" / "Noice Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Wt: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2000" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_2000():
    path = ROOT / "raw-data" / "2000" / "senior" / "Senior Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Wt: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        sections = [section.replace("\n\n", "\n") for section in sections]
        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2000" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def novice_2001():
    path = ROOT / "raw-data" / "2001" / "novice" / "novice.htm"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous_sibling("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Wt: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 4:
            raise RuntimeError("Unexpected <pre>", weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2001" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_2001():
    path = ROOT / "raw-data" / "2001" / "senior" / "senior.htm"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous_sibling("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Wt: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[4:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 4:
            raise RuntimeError("Unexpected <pre>", weight)

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2001" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def novice_2002():
    path = ROOT / "raw-data" / "2002" / "novice" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Weight: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[8:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        championship, consolation, remaining = sections
        remaining_lines = remaining.split("\n")
        if len(remaining_lines) != 10:
            raise RuntimeError("Unexpected <pre>", len(remaining_lines), weight)

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2002" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_2002():
    path = ROOT / "raw-data" / "2002" / "senior" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Weight: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[8:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        championship, consolation, remaining = sections
        remaining_lines = remaining.split("\n")
        if len(remaining_lines) != 10:
            raise RuntimeError("Unexpected <pre>", len(remaining_lines), weight)

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2002" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def novice_2003():
    path = ROOT / "raw-data" / "2003" / "novice" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Weight: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[8:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        championship, consolation, remaining = sections
        remaining_lines = remaining.split("\n")
        if len(remaining_lines) != 10:
            raise RuntimeError("Unexpected <pre>", len(remaining_lines), weight)

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2003" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_2003():
    path = ROOT / "raw-data" / "2003" / "senior" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Weight: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[8:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        championship, consolation, remaining = sections
        remaining_lines = remaining.split("\n")
        if len(remaining_lines) != 10:
            raise RuntimeError("Unexpected <pre>", len(remaining_lines), weight)

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2003" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def _replace_extra_bouts(value, lowest, highest, replace_with):
    for bout_number in range(lowest, highest + 1):
        to_replace = f"Bout:   {bout_number}"
        value = value.replace(to_replace, replace_with)
    return value


def novice_2004():
    weights_pre = {}
    weights = (62, 66, 70, 74, 79, 84, 89, 95, 101, 108, 115, 122, 130, 147, 166, 215)
    path_prefix = ROOT / "raw-data" / "2004" / "novice"

    for weight in weights:
        path = path_prefix / f"Weight Class_ {weight}.html"
        with open(path, "rb") as file_obj:
            raw_bytes = file_obj.read()

        detected = chardet.detect(raw_bytes)
        encoding = detected["encoding"]
        html = raw_bytes.decode(encoding)
        soup = bs4.BeautifulSoup(html, features="html.parser")

        (pre,) = soup.find_all("pre")
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        championship, consolation, remaining = sections
        consolation = _replace_extra_bouts(consolation, 513, 576, "    Bye    ")
        consolation = _replace_extra_bouts(consolation, 577, 640, "           ")

        remaining_lines = remaining.split("\n")
        if len(remaining_lines) != 10:
            raise RuntimeError("Unexpected <pre>", len(remaining_lines), weight)

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2004" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_2004():
    weights_pre = {}
    weights = (
        70,
        74,
        79,
        84,
        89,
        95,
        101,
        108,
        115,
        122,
        130,
        138,
        147,
        156,
        166,
        177,
        189,
        215,
        275,
    )
    path_prefix = ROOT / "raw-data" / "2004" / "senior"

    for weight in weights:
        path = path_prefix / f"Weight Class_ {weight}.html"
        with open(path, "rb") as file_obj:
            raw_bytes = file_obj.read()

        detected = chardet.detect(raw_bytes)
        encoding = detected["encoding"]
        html = raw_bytes.decode(encoding)
        soup = bs4.BeautifulSoup(html, features="html.parser")

        (pre,) = soup.find_all("pre")
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        championship, consolation, remaining = sections
        consolation = _replace_extra_bouts(consolation, 609, 684, "    Bye    ")
        consolation = _replace_extra_bouts(consolation, 685, 760, "           ")

        remaining_lines = remaining.split("\n")
        if len(remaining_lines) != 10:
            raise RuntimeError("Unexpected <pre>", len(remaining_lines), weight)

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2004" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def novice_2005():
    weights_pre = {}
    weights = (62, 66, 70, 74, 79, 84, 89, 95, 101, 108, 115, 122, 130, 147, 166, 215)
    path_prefix = ROOT / "raw-data" / "2005" / "novice"

    for weight in weights:
        path = path_prefix / f"Weight Class_ {weight}.html"
        with open(path, "rb") as file_obj:
            raw_bytes = file_obj.read()

        detected = chardet.detect(raw_bytes)
        encoding = detected["encoding"]
        html = raw_bytes.decode(encoding)
        soup = bs4.BeautifulSoup(html, features="html.parser")

        (pre,) = soup.find_all("pre")
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        pre_text_lines = pre_text.split("\n")
        if len(pre_text_lines) != 68:
            raise RuntimeError("Unexpected <pre>", len(pre_text_lines), weight)

        championship = "\n".join(pre_text_lines[:41])
        consolation = "\n".join(pre_text_lines[41:57])
        assert pre_text_lines[57] == ""
        remaining_lines = pre_text_lines[58:]

        consolation = _replace_extra_bouts(consolation, 513, 576, "    Bye    ")
        consolation = _replace_extra_bouts(consolation, 577, 640, "           ")

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2005" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_2005():
    weights_pre = {}
    weights = (
        70,
        74,
        79,
        84,
        89,
        95,
        101,
        108,
        115,
        122,
        130,
        138,
        147,
        156,
        166,
        177,
        189,
        215,
        275,
    )
    path_prefix = ROOT / "raw-data" / "2005" / "senior"

    for weight in weights:
        path = path_prefix / f"Weight Class_ {weight}.html"
        with open(path, "rb") as file_obj:
            raw_bytes = file_obj.read()

        detected = chardet.detect(raw_bytes)
        encoding = detected["encoding"]
        html = raw_bytes.decode(encoding)
        soup = bs4.BeautifulSoup(html, features="html.parser")

        (pre,) = soup.find_all("pre")
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        pre_text_lines = pre_text.split("\n")
        if len(pre_text_lines) != 68:
            raise RuntimeError("Unexpected <pre>", len(pre_text_lines), weight)

        championship = "\n".join(pre_text_lines[:41])
        consolation = "\n".join(pre_text_lines[41:57])
        assert pre_text_lines[57] == ""
        remaining_lines = pre_text_lines[58:]

        consolation = _replace_extra_bouts(consolation, 609, 684, "    Bye    ")
        consolation = _replace_extra_bouts(consolation, 685, 760, "           ")

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2005" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def novice_2006():
    path = ROOT / "raw-data" / "2006" / "novice" / "Brackets.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Weight: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[8:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        championship, consolation, remaining = sections
        remaining_lines = remaining.split("\n")
        if len(remaining_lines) != 10:
            raise RuntimeError("Unexpected <pre>", len(remaining_lines), weight)

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2006" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_2006():
    path = ROOT / "raw-data" / "2006" / "senior" / "Brackets-2006.html"
    with open(path) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_brackets = soup.find_all("pre")

    weights_pre = {}
    for pre in all_brackets:
        prev_h3 = pre.find_previous("h3")
        if prev_h3 is None:
            raise RuntimeError("Invariant violation", pre)

        weight_text = prev_h3.text
        if not weight_text.startswith("Weight: "):
            raise RuntimeError("Invariant violation", weight_text)

        weight = int(weight_text[8:])
        if weight in weights_pre:
            raise KeyError(weight)
        weights_pre[weight] = pre.text

    weights = sorted(weights_pre.keys())
    for weight in weights:
        pre_text = weights_pre[weight]
        sections = pre_text.split("\n\n")
        if len(sections) != 3:
            raise RuntimeError("Unexpected <pre>", len(sections), weight)

        championship, consolation, remaining = sections
        remaining_lines = remaining.split("\n")
        if len(remaining_lines) != 10:
            raise RuntimeError("Unexpected <pre>", len(remaining_lines), weight)

        before, after = remaining_lines[0].split("-+ ", 1)
        start_fifth = len(before) + after.index(" -") + 4

        fifth_place_lines = []
        seventh_place_lines = []
        for line in remaining_lines[:4]:
            seventh_place_lines.append(line[:start_fifth].rstrip())
            fifth_place_lines.append(line[start_fifth:])

        fifth_place = "\n".join(fifth_place_lines)
        seventh_place = "\n".join(seventh_place_lines)
        # NOTE: The placewinners are in "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2006" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def main():
    junior_iwf_1999()
    novice_iwf_1999()
    senior_iwf_1999()
    junior_iwf_2000()
    novice_iwf_2000()
    senior_iwf_2000()
    novice_2000()
    senior_2000()
    # junior_iwf_2001()
    # novice_iwf_2001()
    # senior_iwf_2001()
    novice_2001()
    senior_2001()
    novice_2002()
    senior_2002()
    novice_2003()
    senior_2003()
    novice_2004()
    senior_2004()
    novice_2005()
    senior_2005()
    novice_2006()
    senior_2006()


if __name__ == "__main__":
    main()
