"""Utilities."""

import re

import ivy

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

# Regex to turn multiple whitespace characters into a single space.
MULTISPACE = re.compile(r"\s+", re.DOTALL)


def fail(msg):
    """Fail unilaterally."""
    raise AssertionError(msg)


def mccole():
    """Get configuration section, creating if necessary."""
    return ivy.site.config.setdefault("mccole", {})


def require(cond, msg):
    """Fail if condition untrue."""
    assert cond, msg
