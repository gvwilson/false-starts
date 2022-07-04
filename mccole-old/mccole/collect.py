"""Collect pages to be transformed."""

import os
from types import SimpleNamespace as SN

from .accounting import Info
from .util import McColeExc

# Main filename for each chapter.
MAIN_SRC_FILE = "index.md"
MAIN_DST_FILE = "index.html"


def collect_pages(config):
    """Return page information."""
    if not config.chapters:
        return []

    major = 0
    result = []

    if config.root:
        result.append(
            Info(
                slug="_index",
                to_root=os.curdir,
                src=os.path.join(config.src, config.root),
                dst=os.path.join(config.dst, "index.html"),
                major=None,
                metadata={},
                template="index.html",
                tokens=None,
            )
        )

    for entry in config.chapters:
        major = _next_major(entry, major)
        try:
            result.append(
                Info(
                    slug=entry["slug"],
                    to_root=os.pardir,
                    src=_src_path(config, entry),
                    dst=_dst_path(config, entry),
                    lede=entry.get("lede", ""),
                    major=major,
                    metadata={},
                    title=entry["title"],
                    template=entry.get("template", None),
                    tokens=None,
                )
            )
        except KeyError as exc:
            raise McColeExc(f"Missing entry {exc} in configuration for {entry}.")

    config.pages = result


# ----------------------------------------------------------------------


def _dst_path(config, entry):
    """Construct output path for entry."""
    return os.path.join(config.dst, entry["slug"], MAIN_DST_FILE)


def _next_major(entry, major):
    """Create next major heading index."""
    # First appendix.
    if entry.get("appendix", False):
        return "A"

    # Chapters are numbered.
    if isinstance(major, int):
        return major + 1

    # Appendices are lettered.
    assert isinstance(major, str) and (len(major) == 1)
    return chr(ord(major) + 1)


def _src_path(config, entry):
    """Construct input path for entry."""
    # Explicit source file (e.g., "LICENSE.md" => "license/index.md").
    if "file" in entry:
        return os.path.join(config.src, entry["file"])

    # Default source file.
    return os.path.join(config.src, entry["slug"], MAIN_SRC_FILE)
