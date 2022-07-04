"""Check consistency of project."""

import re

MAX_CODE_LINES = 120
MAX_LINE_LENGTH = 120


def check(options, config, xref, seen):
    """Check various aspects of project."""
    if "bib" in options.check:
        _check_bib(config, seen)

    if "code" in options.check:
        _check_code(config)

    if "gloss" in options.check:
        _check_gloss(config, seen)


# ----------------------------------------------------------------------


def _check_bib(config, seen):
    """Check consistency of bibliography."""
    _show_unused("biblography", config.bib_keys - seen.cite)

    key = re.compile(r"^[A-Z][A-Za-z]+\d{4}[a-z]?$")
    previous = None
    for entry in config.bib_data:
        # Alphabetic order by key (ignoring case).
        if previous and (previous["ID"].lower() > entry["ID"].lower()):
            print(f"Bibliography entry {entry['ID']} out of order.")
        previous = entry

        # Keys are Name and 4-digit year.
        if not key.match(entry["ID"]):
            print(f"Badly-formatted bibliography key {entry['ID']}.")


def _check_code(config):
    """Check code inclusions."""
    pre = re.compile(
        r'<pre\s+title="(.*?)"><code\s+class="(.*?)">(.*?)</code></pre>', re.DOTALL
    )
    lang = re.compile(r"^language-.+$")
    for info in config.pages:
        for (title, cls, body) in pre.findall(info.html):
            body = body.split("\n")

            # Code class.
            if not lang.search(cls):
                print(
                    f"Code block {title} in {info.src} has unrecognized class {cls}."
                )

            # Number of lines.
            if len(body) > MAX_CODE_LINES:
                print(
                    f"Code block {title} in {info.src} has {len(body)} lines (> {MAX_CODE_LINES})."
                )

            # Line length.
            long_lines = [x for x in body if len(x) > MAX_LINE_LENGTH]
            if long_lines:
                print(
                    f"Code block {title} in {info.src} has {len(long_lines)} long lines (> {MAX_LINE_LENGTH})."
                )


def _check_gloss(config, seen):
    """Check consistency of glossary."""
    _show_unused("glossary", config.gloss_keys - seen.gloss_ref)

    previous = None
    lang = config.lang
    for entry in config.gloss_data:
        # Alphabetic order by key (ignoring case).
        if previous and (previous[lang]["term"].lower() > entry[lang]["term"].lower()):
            print(f"Glossary entry {entry[lang]['key']} out of order.")
        previous = entry


def _show_unused(kind, unused):
    if not unused:
        return
    print(f"Unused {kind} keys:")
    for key in sorted(unused):
        print(f"- {key}")
