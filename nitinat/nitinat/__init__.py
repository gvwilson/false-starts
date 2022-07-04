"""Nitinat: a model data analysis project in Python."""

__version__ = "0.1.0"
__author__ = "Greg Wilson"

import logging
import time
from pathlib import Path

CONFIG = {
    "LOGGER": None,
    "LOGGING_NAME": "Nitinat",
    "LOGGING_LEVEL": "warn",
    "PARAMETERS": Path(__file__).parent.parent.joinpath("parameters"),
}


def get_logger():
    """Get the logger used by this module."""
    if CONFIG["LOGGER"] is None:
        name = CONFIG["LOGGING_NAME"]
        logger = logging.getLogger(name)
        logger.setLevel(CONFIG["LOGGING_LEVEL"].upper())
        formatter = logging.Formatter(
            fmt=f"{name} %(asctime)s %(message)s",
            datefmt="%y-%m-%d:%H:%M:%S",
        )
        formatter.converter = time.gmtime
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        CONFIG["LOGGER"] = logger
    return CONFIG["LOGGER"]
