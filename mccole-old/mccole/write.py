"""Write outputs."""

import logging
import os
from fnmatch import fnmatch
from glob import glob
from pathlib import Path

from .accounting import Info, Seen
from .render import render
from .template import fill_template, make_site_object
from .tokenize import make_markdown_links
from .util import LOGGER_NAME, make_md

# Directory permissions.
DIR_PERMS = 0o755

# Character encoding.
ENCODING = "utf-8"

# Where to report.
LOGGER = logging.getLogger(LOGGER_NAME)


# ----------------------------------------------------------------------


def copy_files(config):
    """Copy static files."""
    for pattern in config.copy:
        filenames = glob(os.path.join(config.src, pattern))
        filenames = [
            f for f in filenames if not any(fnmatch(f, p) for p in config.exclude)
        ]
        filenames = [_pair_src_dst(config, f) for f in filenames]
        for (src_path, dst_path) in filenames:
            LOGGER.info(f"copying {src_path} to {dst_path}")
            _copy_file(src_path, dst_path)


def generate_pages(config, xref, write=True):
    """Generate output for each chapter in turn, filling in cross-references."""
    seen = Seen()
    site = make_site_object(config, seen)
    for info in config.pages:
        html = render(config, xref, seen, info)
        info.html = fill_template(config, xref, info, site, html)
        if write:
            _write_file(info.dst, info.html)
    return seen


def generate_onepage(config, xref, filename):
    """Generate a single-page version."""
    seen = Seen()
    site = make_site_object(config, seen)
    combined = _concatenate_pages(config)
    md = make_md()
    tokens = md.parse(combined)
    info = Info(template="all.html", tokens=tokens)
    html = render(config, xref, seen, info, False)
    html = fill_template(config, xref, info, site, html)
    filename = os.path.join(config.dst, filename)
    _write_file(filename, html)


# ----------------------------------------------------------------------


def _concatenate_pages(config):
    """Combined all pages into one."""
    links = make_markdown_links(config)
    temp = []
    for info in config.pages:
        if info.major:
            temp.append(f'\n<section id="{info.slug}">\n')
            temp.append(f'# {info.title} {{#{info.slug}}}\n')
        temp.append(info.text)
        if info.major:
            temp.append(f"\n</section>\n")
    return "\n".join(temp) + f"\n{links}"


def _copy_file(src, dst):
    """Copy a file without modification, making directories as needed."""
    LOGGER.debug(f"Copying {dst}.")
    dst = Path(dst)
    dst.parent.mkdir(mode=DIR_PERMS, parents=True, exist_ok=True)
    dst.write_bytes(Path(src).read_bytes())


def _pair_src_dst(config, src_file):
    """Construct a pair (src_file, dst_file)."""
    dst_file = os.path.normpath(src_file.replace(config.src, config.dst, 1))
    return (src_file, dst_file)


def _write_file(dst, html):
    """Write a file, making directories if needed."""
    LOGGER.debug(f"Writing {dst}.")
    dst = Path(dst)
    dst.parent.mkdir(mode=DIR_PERMS, parents=True, exist_ok=True)
    dst.write_text(html, encoding=ENCODING)
