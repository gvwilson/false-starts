"""Model parameters."""

import json
from pathlib import Path

from pydantic import BaseModel, validator

from . import CONFIG


class FractionSelectorParameters(BaseModel):
    """Select a fixed fraction of rows at random."""

    fraction: float

    @validator("fraction")
    def fraction_in_range(cls, value):
        if 0 <= value <= 1.0:
            return value
        raise ValueError(f"Fraction must be in [0..1], not {value}")


class NthSelectorParameters(BaseModel):
    """Select every N'th row."""

    stride: int

    @validator("stride")
    def stride_is_legal(cls, value):
        if 1 <= value:
            return value
        raise ValueError(f"Stride must be positive not {value}")


class Parameters:
    """Instantiate model parameters with caching."""

    # (class, filename) => object
    _cache = {}

    @staticmethod
    def get(cls, filename):
        """Return model parameters object with caching."""
        if (cls, filename) not in Parameters._cache:
            path = Path(CONFIG["PARAMETERS"], filename)
            values = Parameters._load_json(path)
            Parameters._cache[(cls, filename)] = cls(**values)
        return Parameters._cache[(cls, filename)]

    @staticmethod
    def clear():
        Parameters._cache.clear()

    @staticmethod
    def _load_json(path):
        with open(path, "r") as reader:
            return json.load(reader)
