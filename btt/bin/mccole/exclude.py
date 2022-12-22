"""Handle file exclusions."""

from fnmatch import fnmatch
from pathlib import Path

import ivy
from util import read_directives


@ivy.filters.register(ivy.filters.Filter.LOAD_NODE_FILE)
def keep_file(value, filepath):
    """Only process the right kinds of files."""
    return not _ignore(Path(filepath).parent, filepath)


@ivy.filters.register(ivy.filters.Filter.LOAD_NODE_DIR)
def keep_dir(value, dirpath):
    """Do not process directories excluded by parent."""
    return not _ignore(Path(dirpath).parent, dirpath)


def _ignore(dirpath, filepath):
    """Check for pattern-based exclusion."""
    directives = read_directives(dirpath, "exclude")
    configured = ivy.site.config.get("exclude", [])
    combined = directives + configured
    return any(fnmatch(filepath.name, pat) for pat in combined)
