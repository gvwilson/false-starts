"""Shared fixtures."""

from pytest import fixture

from nitinat.parameters import Parameters


@fixture
def clear_cache():
    Parameters.clear()
