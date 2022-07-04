"""Test parameter loading."""

from unittest.mock import patch

import pytest

from nitinat.parameters import (
    FractionSelectorParameters,
    NthSelectorParameters,
    Parameters,
)

LOAD_JSON = "nitinat.parameters.Parameters._load_json"


def test_parameters_fraction_load(clear_cache):
    parameters = Parameters.get(FractionSelectorParameters, "fraction-0.1.json")
    assert parameters.fraction == 0.1


def test_parameters_fraction_invalid_negative(clear_cache):
    with patch(LOAD_JSON, return_value={"fraction": -0.1}):
        with pytest.raises(ValueError):
            Parameters.get(FractionSelectorParameters, "fraction.json")


def test_parameters_fraction_invalid_large(clear_cache):
    with patch(LOAD_JSON, return_value={"fraction": 1.1}):
        with pytest.raises(ValueError):
            Parameters.get(FractionSelectorParameters, "fraction.json")


def test_parameters_nth_load(clear_cache):
    parameters = Parameters.get(NthSelectorParameters, "nth-50.json")
    assert parameters.stride == 50


def test_parameters_nth_invalid_stride_low(clear_cache):
    with patch(LOAD_JSON, return_value={"stride": 0}):
        with pytest.raises(ValueError):
            Parameters.get(NthSelectorParameters, "nth.json")


def test_parameters_objects_are_recycled(clear_cache):
    parameters = [
        Parameters.get(NthSelectorParameters, "nth-50.json") for i in range(3)
    ]
    assert all(id(p) == id(parameters[0]) for p in parameters)


def test_parameters_load_called_once(clear_cache):
    with patch(LOAD_JSON, return_value={"stride": 50}) as mock:
        [Parameters.get(NthSelectorParameters, "nth-50.json") for i in range(3)]
    assert mock.call_count == 1
