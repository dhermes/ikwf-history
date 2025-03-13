import pathlib

import bs4

HERE = pathlib.Path(__file__).resolve().parent


def novice_2001():
    path = HERE / ".." / "raw-data" / "2001" / "novice" / "novice.htm"
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
    path = HERE / ".." / "raw-data" / "2001" / "senior" / "senior.htm"
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


def novice_2003():
    path = HERE / ".." / "raw-data" / "2003" / "novice" / "Brackets.html"
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
        placers = "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
            placers,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2003" / "novice" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def senior_2003():
    path = HERE / ".." / "raw-data" / "2003" / "senior" / "Brackets.html"
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
        placers = "\n".join(remaining_lines[4:])

        sections_final = [
            championship,
            consolation,
            fifth_place,
            seventh_place,
            placers,
        ]

        new_html = "<hr>".join([f"<pre>{section}</pre>" for section in sections_final])
        new_html = f"<html><body>{new_html}</body></html>"

        new_path = HERE / "2003" / "senior" / f"{weight}.html"
        with open(new_path, "w") as file_obj:
            file_obj.write(new_html)


def main():
    novice_2001()
    senior_2001()
    novice_2003()
    senior_2003()


if __name__ == "__main__":
    main()
