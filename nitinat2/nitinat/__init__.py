"""Nitinat: a model data analysis project in Python."""

__version__ = "0.1.0"
__author__ = "Greg Wilson"

from pathlib import Path

CONFIG = {
    "cache": Path(__file__).parent.parent.joinpath("cache"),
    "remote": Path(__file__).parent.parent.joinpath("remote"),
}
