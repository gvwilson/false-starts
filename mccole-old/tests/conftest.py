"""Shared fixtures."""

from types import SimpleNamespace as SN

import pytest

from mccole.config import DEFAULT_CONFIG_FILE


@pytest.fixture
def options():
    """Minimal runnable options."""
    return SN(config=DEFAULT_CONFIG_FILE)
