"""Create cross-reference lookup."""

import logging
from types import SimpleNamespace as SN

from .accounting import CrossRef
from .patterns import (
    FIGURE,
    FIGURE_CAP,
    FIGURE_ID,
    FIGURE_INFO,
    HEADING_ID,
    TABLE_BODY,
    TABLE_CAP,
    TABLE_ID,
    TABLE_START,
)
from .util import LOGGER_NAME, err

# Where to report.
LOGGER = logging.getLogger(LOGGER_NAME)


def cross_reference(config):
    """Create cross-reference tables for all pages."""
    # Exclude un-indexed pages (e.g., home page).
    pages = [p for p in config.pages if p.major is not None]

    xref = CrossRef()
    _headings(config, xref, pages)
    _figures(config, xref, pages)
    _tables(config, xref, pages)

    return xref


# ----------------------------------------------------------------------


def _figures(config, xref, pages):
    """Build cross-references for figures."""
    for info in pages:
        current = [info.major, 0]

        for token in info.tokens:
            if token.type != "html_block":
                continue

            match = FIGURE.search(token.content)
            if not match:
                continue

            fig_id = FIGURE_ID.search(match.group(0))
            if not fig_id:
                continue

            if not FIGURE_INFO.search(match.group(0)):
                err(f"Badly-formatted figure img {match.group(0)}", info, token)
                continue

            if not FIGURE_CAP.search(match.group(0)):
                err(f"Badly-formatted figure caption {match.group(0)}", info, token)
                continue

            fig_id = fig_id.group(1)
            if fig_id in xref.fig_id_to_index:
                err(f"Duplicate figure label '{fig_id}'", info, token)

            current[1] += 1
            label = tuple(current)
            xref.fig_id_to_index[fig_id] = label
            xref.fig_id_to_slug[fig_id] = info.slug


def _headings(config, xref, pages):
    """Compile headings."""
    blockquote_depth = 0
    for info in pages:
        # Level-1 heading
        slug = info.slug
        info_id = str(info.major)
        info.major = info_id
        xref.hd_id_to_index[slug] = (info_id,)
        xref.hd_id_to_slug[slug] = slug
        xref.hd_id_to_title[slug] = info.title
        xref.hd_index_to_id[(info_id,)] = slug

        # Collect other headings
        label_stack = [info.major]
        previous = None
        for token in info.tokens:
            # Keep track of blockquote nesting to prevent spurious warnings
            # about heading levels
            if token.type == "blockquote_open":
                blockquote_depth += 1
            elif token.type == "blockquote_close":
                blockquote_depth -= 1

            # Ignore everything that isn't a heading
            if (previous is None) or (previous.type != "heading_open"):
                previous = token
                continue

            assert token.type == "inline"

            title, label = _heading_info(token)
            level = _heading_level(info, previous)
            index = _heading_index(
                config, info, token, label_stack, level, blockquote_depth
            )

            # Don't record if not labeling (but have already incremented counter).
            if label:
                if (label in xref.hd_id_to_index) or (label in xref.hd_id_to_title):
                    err(f"Duplicate heading label '{label}'", info, token)
                xref.hd_id_to_index[label] = index
                xref.hd_id_to_title[label] = title
                xref.hd_id_to_slug[label] = info.slug
                xref.hd_index_to_id[index] = label

            previous = token


def _heading_index(config, info, token, stack, level, blockquote_depth):
    """Get the next heading level, adjusting `stack` as a side effect."""
    # Treat chapter titles specially.
    if level == 1:
        return tuple(str(i) for i in stack)

    # Moving up
    if level > len(stack):
        if (level > len(stack) + 1) and (blockquote_depth == 0):
            err(f"Heading {level} out of place", info, token)
        while len(stack) < level:
            stack.append(1)

    # Same level
    elif level == len(stack):
        stack[-1] += 1

    # Going down
    else:
        while len(stack) > level:
            stack.pop()
        stack[-1] += 1

    # Report.
    return tuple(str(i) for i in stack)


def _heading_info(token):
    """Get title and label (or None) from token."""
    assert token.type == "inline"
    match = HEADING_ID.search(token.content)
    if not match:
        return None, None
    return match.group(1), match.group(3)


def _heading_level(info, token):
    """Return the number level of a heading level."""
    tag = token.tag[1]
    level = int(tag)
    return level


def _tables(config, xref, pages):
    """Build cross-references for tables."""
    for info in pages:
        current = [info.major, 0]

        for token in info.tokens:
            if token.type != "html_block":
                continue

            match = TABLE_START.search(token.content)
            if not match:
                continue

            tbl_id = TABLE_ID.search(token.content)
            caption = TABLE_CAP.search(token.content)
            body = TABLE_BODY.search(token.content)
            if not all([tbl_id, caption, body]):
                err("Badly-formatted table", info, token)
                continue

            tbl_id = tbl_id.group(1)
            if tbl_id in xref.tbl_id_to_index:
                err(f"Duplicate table label '{tbl_id}'", info, token)

            current[1] += 1
            label = tuple(current)
            xref.tbl_id_to_index[tbl_id] = label
            xref.tbl_id_to_slug[tbl_id] = info.slug
