"""Generate a glossary."""

import logging
import re

import yaml

from .util import LOGGER_NAME, MISSING, McColeExc, make_md

INTERNAL = re.compile(r"\[(.+?)\]\(#(.+?)\)")
LOGGER = logging.getLogger(LOGGER_NAME)
MULTISPACE = re.compile(r"\s+", re.DOTALL)


class GlossaryEntry:
    """Represent a multilingual glossary entry."""
    def __init__(self, data):
        if (not isinstance(data, dict)) or ("key" not in data):
            raise McColeExc(f"Badly-structured glossary entry {data}")
        self.data = data
        self.key = data["key"]

    def __getitem__(self, keys):
        """Return glossary data."""
        if isinstance(keys, str):
            return self.data[keys]

        assert isinstance(keys, tuple) and (len(keys) == 2)
        lang, subkey = keys
        return self.data[lang][subkey] if lang in self.data else MISSING

    def __setitem__(self, keys, value):
        """Update a glossary sub-entry."""
        assert len(keys) == 2
        lang, subkey = keys
        if lang not in self.data:
            data[lang] = {}
        self.data[lang][subkey] = value

    def __str__(self):
        """Printable representation."""
        return f"gloss(key={self.key}, data={self.data})"


def gloss_to_html(config, seen):
    """Convert glossary data to HTML."""
    if not config.lang:
        raise McColeExc("Cannot convert glossary: no language in configuration.")

    lang = config.lang
    try:
        internal = {entry.key: entry[lang, "term"] for entry in config.gloss_data}
    except KeyError as exc:
        raise McColeExc(f"Glossary entry or entries missing 'key' {exc}.")

    entries = [entry for entry in config.gloss_data]
    entries.sort(key=lambda x: x[lang, "term"].lower())
    entries = [
        _gloss_to_markdown(config, entry, lang, internal, seen)
        for entry in entries
    ]
    text = "\n\n".join(entries)
    md = make_md()
    html = md.render(text)
    return html


def load_gloss(config):
    """Create a glossary from a YAML file."""
    if not config.gloss:
        return

    try:
        with open(config.gloss, "r") as reader:
            raw = yaml.safe_load(reader) or []
            config.gloss_data = [GlossaryEntry(entry) for entry in raw]
    except OSError:
        raise McColeExc(f"Unable to open glossary file {config.gloss}.")

    config.gloss_keys = {entry.key for entry in config.gloss_data}


# ----------------------------------------------------------------------


def _gloss_to_markdown(config, entry, lang, internal, seen):
    """Convert single glossary entry to Markdown."""
    first = f'<span class="glosskey" id="{entry.key}">{entry[lang, "term"]}</span>'

    if "acronym" in entry[lang]:
        first += f" ({entry[lang]['acronym']})"

    body = MULTISPACE.sub(entry[lang, "def"], " ")
    for (text, link) in INTERNAL.findall(body):
        seen.gloss_ref.add(link)

    if "ref" in entry[lang]:
        refs = []
        seealso = config.terms[lang]["seealso"]
        for ref in entry[lang, "ref"]:
            if ref in internal:
                refs.append(ref)
                seen.gloss_ref.add(ref)
            else:
                LOGGER.error(
                    f"Bad cross-reference '{ref}' in glossary entry '{entry}'."
                )
        refs = [f"[{internal[ref]}](#{ref})" for ref in refs]
        body += f"<br/>{seealso}: {', '.join(refs)}."

    result = f"{first}\n:   {body}"
    return result
