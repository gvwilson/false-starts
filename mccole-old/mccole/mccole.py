"""Main entry point."""

import argparse
import logging
import os
import shutil

import pkg_resources

from . import __version__ as version
from .bib import load_bib
from .check import check
from .collect import collect_pages
from .config import DEFAULT_CONFIG_FILE, DEFAULTS, load_config
from .crossref import cross_reference
from .gloss import load_gloss
from .server import run_server
from .show import show
from .tokenize import tokenize
from .util import LOGGER_NAME, McColeExc
from .write import copy_files, generate_onepage, generate_pages

# ----------------------------------------------------------------------


CHECK_CHOICES = ["bib", "code", "gloss"]
LOGGING_LEVELS = "debug info warning error critical".split()
LOGGER = None
SHOW_CHOICES = ["bib", "gloss", "index", "pages", "xref"]


def main(args):
    """Parse arguments and execute."""
    try:
        options = _parse_args(args)

        if options.version:
            print(version)
            return

        if _resources(options):
            return

        _setup(options)
        config = load_config(options)

        load_bib(config)
        load_gloss(config)
        collect_pages(config)
        tokenize(config)
        xref = cross_reference(config)

        if not options.dryrun:
            _clean_output(options, config)
            copy_files(config)

        seen = generate_pages(config, xref, not options.dryrun)
        if options.onepage and not options.dryrun:
            generate_onepage(config, xref, options.onepage)

        show(options, config, xref, seen)
        check(options, config, xref, seen)
        _warn_unused(options, config, xref, seen)

        run_server(options, config.dst)

    except McColeExc as exc:
        LOGGER.error(f"McCole failed: {exc.msg}")


# ----------------------------------------------------------------------


def _clean_output(options, config):
    """Delete output directory unless told not to."""
    if (not options.keep) and os.path.exists(config.dst):
        shutil.rmtree(config.dst)


def _parse_args(args):
    """Handle command-line arguments."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-d", "--dst", type=str, default=DEFAULTS["dst"], help="Destination directory."
    )
    parser.add_argument(
        "-C",
        "--chdir",
        type=str,
        default=None,
        help="Change directory before running.",
    )
    parser.add_argument(
        "--check", nargs="+", default=[], choices=CHECK_CHOICES, help="Check project."
    )
    parser.add_argument(
        "--css",
        action="store_true",
        help="Show standard CSS file.",
    )
    parser.add_argument(
        "--dryrun", action="store_true", help="Do not generate output files."
    )
    parser.add_argument(
        "-g",
        "--config",
        type=str,
        default=DEFAULT_CONFIG_FILE,
        help="Configuration file.",
    )
    parser.add_argument(
        "--js",
        action="store_true",
        help="Show standard JavaScript file.",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep pre-existing output."
    )
    parser.add_argument(
        "-l", "--lang", type=str, default="", help="Specify language (2-letter code)."
    )
    parser.add_argument(
        "-L",
        "--logging",
        type=str,
        choices=LOGGING_LEVELS,
        default="warning",
        help="Logging level.",
    )
    parser.add_argument("-o", "--onepage", type=str, help="Create a single-page version.")
    parser.add_argument("-r", "--run", type=int, help="Run server on specified port.")
    parser.add_argument(
        "--show",
        nargs="+",
        default=[],
        choices=SHOW_CHOICES,
        help="Show internal data for debugging.",
    )
    parser.add_argument(
        "-s", "--src", type=str, default=DEFAULTS["src"], help="Source directory."
    )
    parser.add_argument(
        "--template",
        type=str,
        default="",
        help="Show a template.",
    )
    parser.add_argument(
        "--templates",
        action="store_true",
        help="Show available HTML templates.",
    )
    parser.add_argument(
        "-u",
        "--unused",
        action="count",
        default=0,
        help="Warn about unreferenced items.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version.",
    )

    return parser.parse_args(args)


def _resources(options):
    """Handle requests for resources."""
    if options.css:
        return _show_css()

    if options.js:
        return _show_js()

    if options.template:
        return _show_template(options.template)

    if options.templates:
        return show_template_list()

    return False


def _setup(options):
    """Do initial setup."""
    # Logging.
    global LOGGER
    level_name = options.logging.upper()
    logging.basicConfig(format="%(levelname)s: %(message)s")
    LOGGER = logging.getLogger(LOGGER_NAME)
    LOGGER.setLevel(logging._nameToLevel[level_name])

    # Working directory.
    if options.chdir is not None:
        logging.info(f"changing working directory to {options.chdir}")
        os.chdir(options.chdir)

    LOGGER.info("returning from _setup")


def _show_css():
    """Show standard CSS file."""
    reader = pkg_resources.resource_stream(__name__, "data/mccole.css")
    text = str(reader.read(), encoding="utf-8")
    print(text.rstrip())
    return True


def _show_js():
    """Show standard JavaScript file."""
    reader = pkg_resources.resource_stream(__name__, "data/mccole.js")
    text = str(reader.read(), encoding="utf-8")
    print(text.rstrip())
    return True


def _show_template(filename):
    """Show standard template."""
    try:
        reader = pkg_resources.resource_stream(__name__, f"data/{filename}")
        text = str(reader.read(), encoding="utf-8")
        print(text.rstrip())
    except FileNotFoundError:
        print(f"Unknown template '{filename}'")
    return True


def show_template_list():
    """Show available HTML templates."""
    filenames = pkg_resources.resource_listdir(__name__, "data")
    filenames = [f for f in filenames if f.endswith(".html")]
    if not filenames:
        print("No templates")
    else:
        for f in filenames:
            print(f)
    return True


def _warn_unused(options, config, xref, seen):
    """Warn about unused labels if asked to."""
    for (title, defined_key, used_key) in (
        ("figure", "fig_id_to_index", "figure_ref"),
        ("table", "tbl_id_to_index", "table_ref"),
    ):
        defined = set(getattr(xref, defined_key).keys())
        used = getattr(seen, used_key)
        _warn_unused_title(title, defined - used)


def _warn_unused_title(title, items):
    """Warn about a single set of missing items (if any)."""
    if not items:
        return
    unused = "\n- ".join(sorted(items))
    LOGGER.warning(f"Unreferenced {title}:\n- {unused}")
