"""Handle bibliography."""

import logging
import re

import bibtexparser

from .util import LOGGER_NAME, McColeExc

LOGGER = logging.getLogger(LOGGER_NAME)


def bib_to_html(config):
    """Create HTML version of bibliography data."""
    entries = [_bib_to_html(e, config.lang) for e in config.bib_data]
    return "\n".join(['<div class="bibliography">', "\n".join(entries), "</div>"])


def load_bib(config):
    """Read bibliography file if there is one."""
    if not config.bib:
        return

    try:
        with open(config.bib, "r") as reader:
            entries = bibtexparser.load(reader).entries
            config.bib_data = [_cleanup(entry) for entry in entries]
    except OSError:
        raise McColeExc(f"Unable to open bibliography file {config.bib}.")

    config.bib_keys = {entry["ID"] for entry in config.bib_data}


# ----------------------------------------------------------------------


LATEX = [
    (r'\%', '%'),
    (r'\&', '&'),
    (r'{', ''),
    (r'}', ''),
]


def _cleanup(entry):
    """Remove LaTeXisms in entry."""
    for key in entry:
        for (escape, char) in LATEX:
            entry[key] = entry[key].replace(escape, char)
    return entry


def _bib_to_html(entry, lang):
    """Convert bibliography entry to HTML."""
    kind = entry["ENTRYTYPE"]
    key = entry["ID"]
    content = HANDLERS[kind](entry, lang)
    content = "".join(c for c in content if c is not None)
    cite = f'<span class="bibkey">{key}</span>'
    content = f'<span class="bibentry">{content}</span>'
    return f'<p id="{key}" class="bib">{cite}: {content}</p>'


def _article(entry, lang):
    return [
        _credits(entry),
        ": ",
        _title(entry, quote=True),
        ". ",
        _journal(entry),
        _vol_num(entry, prefix=", "),
        ", ",
        _date(entry),
        ", ",
        _publisher(entry),
        _doi_url(entry, prefix=", "),
        ".",
        _review(entry, lang, prefix=" "),
    ]


def _book(entry, lang):
    if "author" in entry:
        names = _credits(entry)
    else:
        names = _credits(entry, field="editor", suffix="(ed.)")
    return [
        names,
        ": ",
        _title(entry, emph=True),
        " ",
        _publisher(entry),
        ", ",
        _date(entry),
        ", ",
        _isbn(entry),
        ".",
        _review(entry, lang, prefix=" "),
    ]


def _incollection(entry, lang):
    return [
        _credits(entry),
        ": ",
        _title(entry, quote=True),
        ". In ",
        _credits(entry, field="editor", suffix="(ed.)"),
        ": ",
        _booktitle(entry),
        ", ",
        _publisher(entry),
        ", ",
        _date(entry),
        _isbn(entry, prefix=", "),
        ".",
        _review(entry, lang, prefix=" "),
    ]


def _inproceedings(entry, lang):
    return [
        _credits(entry),
        ": ",
        _title(entry, quote=True),
        ". In ",
        _booktitle(entry),
        ", ",
        _date(entry),
        _publisher(entry, prefix=", "),
        ", ",
        _doi_url(entry),
        ".",
        _review(entry, lang, prefix=" "),
    ]


def _misc(entry, lang):
    return [
        _credits(entry),
        ": ",
        _title(entry, quote=True),
        _url(entry, prefix=" "),
        _date(entry, prefix=", viewed "),
        ".",
        _review(entry, lang, prefix=" "),
    ]


HANDLERS = {
    "article": _article,
    "book": _book,
    "incollection": _incollection,
    "inproceedings": _inproceedings,
    "misc": _misc,
}


def _booktitle(entry):
    return f"<em>{entry['booktitle']}</em>"


SPLIT_NAMES = re.compile(r"\band\b")


def _credits(entry, field="author", suffix=None):
    names = [n.strip() for n in SPLIT_NAMES.split(entry[field])]
    if len(names) == 1:
        names = names[0]
    elif len(names) == 2:
        names = f"{names[0]} and {names[1]}"
    else:
        names = ", ".join(names[:-1]) + f", and {names[-1]}"
    if suffix is not None:
        names = f"{names} {suffix}"
    return names


MONTH = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}


def _date(entry, prefix=None):
    if "year" not in entry:
        LOGGER.error(f"Bibliography entry missing year {entry}.")
        return None
    if "month" not in entry:
        result = entry["year"]
    else:
        result = f"{MONTH[entry['month']]} {entry['year']}"
    if prefix is not None:
        result = f"{prefix}{result}"
    return result


def _doi_url(entry, prefix=None):
    if "doi" not in entry:
        return _url(entry, prefix)
    doi = entry["doi"]
    result = _with_prefix(f'<a href="https://doi.org/{doi}">{doi}</a>', prefix)
    return result


def _isbn(entry, prefix=None):
    return _with_prefix(entry.get("isbn", None), prefix)


def _journal(entry):
    return f"<em>{entry['journal']}</em>"


def _publisher(entry, prefix=None):
    return _with_prefix(entry.get("publisher", None), prefix)


def _review(entry, lang, prefix=None):
    if lang not in entry:
        return ""
    text = f'<span class="bibreview">{entry[lang]}</span>'
    return _with_prefix(text, prefix)


def _title(entry, quote=False, emph=False):
    if quote:
        return f'"{entry["title"]}"'
    if emph:
        return f"<em>{entry['title']}</em>"


def _url(entry, prefix=None):
    if "url" not in entry:
        return None
    url = entry["url"]
    result = _with_prefix(f'<a href="{url}">{url}</a>', prefix)
    return result


def _vol_num(entry, prefix=None):
    if "volume" not in entry:
        return None
    if "number" not in entry:
        result = entry["volume"]
    else:
        result = f"{entry['volume']}({entry['number']})"
    return _with_prefix(result, prefix)


def _with_prefix(text, prefix):
    if text is None:
        return text
    elif prefix is None:
        return text
    else:
        return f"{prefix}{text}"
