"""Utilities."""

import json
import logging
import os

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.front_matter import front_matter_plugin

# Identify this module's logger.
LOGGER_NAME = "mccole"

# Where to report.
LOGGER = logging.getLogger(LOGGER_NAME)

# How to report missing items.
MISSING = "MISSING"

# Translated terms.
TRANSLATIONS = {
    "en": {
        "appendix": "Appendix",
        "chapter": "Chapter",
        "figure": "Figure",
        "seealso": "See also",
        "section": "Section",
        "table": "Table"
    },
    "es": {
        "appendix": "Anexo",
        "chapter": "Capítulo",
        "figure": "Figura",
        "seealso": "Ver también",
        "section": "Sección",
        "table": "Tabla"
    }
}


# ----------------------------------------------------------------------


class McColeExc(Exception):
    """Problems we expect."""

    def __init__(self, msg):
        """Save the message."""
        self.msg = msg


def err(msg, info, token=None):
    """Report an error with location information."""
    LOGGER.error(f"{msg} {loc(info, token)}")


def loc(info, token):
    """Report error location in token stream."""
    if (token is None) or (token.map is None):
        return f"({info.src})"
    return f"({info.src}/{token.map[1]})"


def make_inclusion_filename(info, name, slug):
    """Construct full path name."""
    prefix = slug if slug else os.path.dirname(info.src)
    return os.path.join(prefix, name)


def make_md():
    """Make Markdown parser."""
    return (
        MarkdownIt("commonmark")
        .enable("table")
        .use(deflist_plugin)
        .use(front_matter_plugin)
    )
