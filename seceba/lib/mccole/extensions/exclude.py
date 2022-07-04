"""Handle file exclusions."""

from fnmatch import fnmatch

import ivy


@ivy.filters.register(ivy.filters.Filter.LOAD_NODE_DIR)
def exclude(value, filepath):
    """Skip excluded directories."""
    if filepath.joinpath(".ivyignore").exists():
        return False
    if (patterns := ivy.site.config.get("exclude", None)) is None:
        return True
    return not any(fnmatch(filepath, pat) for pat in patterns)


@ivy.filters.register(ivy.filters.Filter.LOAD_NODE_FILE)
def exclude(value, filepath):
    """Skip excluded files."""
    if (patterns := ivy.site.config.get("exclude", None)) is None:
        return True
    return not any(fnmatch(filepath, pat) for pat in patterns)
