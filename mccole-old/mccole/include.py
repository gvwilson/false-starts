"""Handle file inclusion."""

import logging

from .patterns import (
    INCLUSION_FILE,
    INCLUSION_KEEP,
    INCLUSION_KEEP_OMIT,
    INCLUSION_MULTI,
    INCLUSION_OMIT,
)
from .util import LOGGER_NAME, MISSING, make_inclusion_filename, make_md

LOGGER = logging.getLogger(LOGGER_NAME)


def inclusion_to_html(info, spec, slug):
    """Handle a file inclusion."""
    for (pat, handler) in (
        (INCLUSION_FILE, _file),
        (INCLUSION_KEEP, _keep),
        (INCLUSION_OMIT, _omit),
        (INCLUSION_KEEP_OMIT, _keep_omit),
        (INCLUSION_MULTI, _multi),
    ):
        match = pat.search(spec)
        if match:
            return handler(info, match, slug)
    where = info.src
    if slug is not None:
        where += "/" + slug
    LOGGER.error(f"Unrecognized inclusion spec '{spec}' in {where}.")
    return ""


# ----------------------------------------------------------------------


def _file(info, match, slug):
    """Handle a simple file inclusion."""
    title = match.group(1)
    filename = make_inclusion_filename(info, title, slug)
    return _include_file(filename, title)


def _keep(info, match, slug):
    """Handle a sliced file inclusion."""
    title = match.group(1)
    filename = make_inclusion_filename(info, title, slug)
    key = match.group(2)
    return _include_file(filename, title, lambda lns: _keep_lines(lns, key))


def _keep_omit(info, match, slug):
    """Handle an inclusion that keeps some content but omits other."""
    title = match.group(1)
    filename = make_inclusion_filename(info, title, slug)
    keep_key = match.group(2)
    omit_key = match.group(3)
    return _include_file(
        filename,
        title,
        lambda lns: _keep_lines(lns, keep_key),
        lambda lns: _omit_lines(lns, omit_key),
    )


def _multi(info, match, slug):
    """Handle multiple file inclusion."""
    result = []
    pat = match.group(1)
    for fill in [s.strip() for s in match.group(2).split()]:
        title = pat.replace("*", fill)
        filename = make_inclusion_filename(info, title, slug)
        kind = filename.split(".")[-1]
        with open(filename, "r") as reader:
            lines = reader.readlines()
            result.append(_make_html(filename, title, kind, lines))
    return "\n\n".join(result)


def _omit(info, match, slug):
    """Handle an erasing file inclusion."""
    title = match.group(1)
    filename = make_inclusion_filename(info, title, slug)
    key = match.group(2)
    return _include_file(filename, title, lambda lns: _omit_lines(lns, key))


# ----------------------------------------------------------------------


def _find_markers(lines, key):
    start = f"[{key}]"
    stop = f"[/{key}]"
    i_start = None
    i_stop = None
    for (i, line) in enumerate(lines):
        if start in line:
            i_start = i
        elif stop in line:
            i_stop = i
    return i_start, i_stop


def _include_file(filename, title, *filters):
    kind = filename.split(".")[-1]
    try:
        with open(filename, "r") as reader:
            lines = reader.readlines()
            for f in filters:
                lines = f(lines)
            return _make_html(filename, title, kind, lines)
    except OSError:
        LOGGER.error(f"Unable to read inclusion '{filename}'.")
        return MISSING


def _keep_lines(lines, key):
    """Select lines between markers."""
    start, stop = _find_markers(lines, key)
    if (start is None) or (stop is None):
        LOGGER.error(f"Failed to match inclusion 'keep' key {key}")
        return []
    return lines[start + 1 : stop]  # noqa e203


def _make_html(filename, title, kind, lines):
    """Construct HTML inclusion from lines."""
    body = "\n".join(x.rstrip() for x in lines)
    markdown = f"```{kind}\n{body}\n```"
    md = make_md()
    html = md.render(markdown)
    html = html.replace("<pre>", f'<pre title="{title}">')
    return html


def _omit_lines(lines, key):
    """Remove lines between markers."""
    start, stop = _find_markers(lines, key)
    if (start is None) or (stop is None):
        LOGGER.error(f"Failed to match inclusion 'omit' key {key}")
        return []
    return lines[:start] + lines[stop + 1 :]  # noqa e203
