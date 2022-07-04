"""Manage program configuration."""

import logging
import os
from datetime import datetime
from types import SimpleNamespace

import yaml

from .accounting import Config
from .template import load_templates
from .util import LOGGER_NAME, TRANSLATIONS, McColeExc

LOGGER = logging.getLogger(LOGGER_NAME)


# Where to look for configuration.
DEFAULT_CONFIG_FILE = "mccole.yml"

# Default configuration settings.
DEFAULTS = {
    "src": os.curdir,  # Process current directory.
    "dst": "docs",  # Write HTML to `_site`.
    "exclude": [DEFAULT_CONFIG_FILE, ".git", "*~", ".DS_Store"],  # Don't copy these.
}


def load_config(options):
    """Read configuration file."""
    try:
        with open(options.config, "r") as reader:
            config = yaml.safe_load(reader) or {}
            config = DEFAULTS | config
            config = Config(**config)

            if hasattr(options, "src"):
                config.src = options.src

            if hasattr(options, "dst"):
                config.dst = options.dst

            if options.lang:
                config.lang = options.lang
            if config.lang not in TRANSLATIONS:
                raise McColeExc(f"Unknown language '{config.lang}'")

            if config.links:
                config.links_data = _read_links(config.links)

            load_templates(config)

            return config

    except OSError as exc:
        raise McColeExc(str(exc))


# ----------------------------------------------------------------------


def _read_links(filename):
    """Read YAML links file for later use."""
    with open(filename, "r") as reader:
        return yaml.safe_load(reader)
