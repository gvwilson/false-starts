"""Handle file exclusions."""

from fnmatch import fnmatch

import ivy
import shortcodes
import util


@ivy.filters.register(ivy.filters.Filter.LOAD_NODE_FILE)
def exclude(value, filepath):
    """Only process HTML and Markdown files."""
    if (patterns := ivy.site.config.get("exclude", None)) is None:
        return True
    return not any(fnmatch(filepath, pat) for pat in patterns)
