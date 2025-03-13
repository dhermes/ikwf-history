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


def main():
    novice_2001()
    senior_2001()


if __name__ == "__main__":
    main()
