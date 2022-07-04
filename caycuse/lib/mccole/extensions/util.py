"""Utilities."""

import re
import sys

import ivy

# Configuration sections and their default values.
# These are added to the config dynamically under the `mccole` key,
# i.e., `"figures"` becomes `ivy.site.config["mccole"]["figures"]`.
CONFIGURATIONS = {
    "bibliography": set(),  # citations
    "figures": {},  # numbered figures
    "glossary": set(),  # glossary keys
    "headings": {},  # number chapter, section, and appendix headings
}

# Translations of multilingual terms.
TRANSLATIONS = {
    "en": {
        "appendix": "Appendix",
        "chapter": "Chapter",
        "figure": "Figure",
        "seealso": "See also",
        "section": "Section",
        "table": "Table",
    },
    "es": {
        "appendix": "Anexo",
        "chapter": "Capítulo",
        "figure": "Figura",
        "seealso": "Ver también",
        "section": "Sección",
        "table": "Tabla",
    },
}

# Regex to match a Markdown heading with optional attributes.
HEADING = re.compile(r"^(#+)\s*(.+?)(\{:\s*#(.+\b)\})?$", re.MULTILINE)

# Regex to turn multiple whitespace characters into a single space.
MULTISPACE = re.compile(r"\s+", re.DOTALL)


def fail(msg):
    """Fail unilaterally."""
    raise AssertionError(msg)


def get_config(part):
    """Get configuration subsection or `None`.

    A result of `None` indicates that the request is being made
    too early in the processing cycle.
    """
    if part not in CONFIGURATIONS:
        fail(f"Unknown configuration section '{part}'")
    mccole = ivy.site.config.setdefault("mccole", {})
    return mccole.get(part, None)


def make_config(part, filler=None):
    """Make configuration subsection.

    If `filler` is not `None`, it is used as the initial value.
    Otherwise, the value from `CONFIGURATIONS` is used.
    """
    if part not in CONFIGURATIONS:
        fail(f"Unknown configuration section '{part}'")
    filler = filler if (filler is not None) else CONFIGURATIONS[part]
    return ivy.site.config.setdefault("mccole", {}).setdefault(part, filler)


def make_label(kind, number):
    """Create numbered labels for figures, tables, and document parts."""
    translations = TRANSLATIONS[ivy.site.config["lang"]]
    if kind == "figure":
        name = translations["figure"]
    elif kind == "part":
        if len(number) > 1:
            name = translations["section"]
        elif number[0].isdigit():
            name = translations["chapter"]
        else:
            name = translations["appendix"]
    elif kind == "table":
        name = translations["table"]
    else:
        fail(f"Unknown kind of label {kind}")

    number = ".".join(number)
    return f"{name} {number}"


def make_major():
    """Construct major numbers/letters based on configuration.

    This function relies on the configuration containing `"chapters"`
    and `"appendices"`, which must be lists of slugs.
    """
    chapters = {slug: i + 1 for (i, slug) in enumerate(ivy.site.config["chapters"])}
    appendices = {
        slug: chr(ord("A") + i)
        for (i, slug) in enumerate(ivy.site.config["appendices"])
    }
    return chapters | appendices


def mccole():
    """Get configuration section, creating if necessary."""
    return ivy.site.config.setdefault("mccole", {})


def require(cond, msg):
    """Fail if condition untrue."""
    assert cond, msg


def report(title, items):
    """Report missing or unused items."""
    if not ivy.site.config.get("warnings", False):
        return
    if not items:
        return
    print(title)
    for i in sorted(items):
        print(f"-  {i}")


def warn(msg):
    """Print a unilateral warning."""
    print(msg, file=sys.stderr)
