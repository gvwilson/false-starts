"""Test data-handling functions."""

from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd
from pytest import fixture

from nitinat.data import COLUMNS, clean_raw_data, read_clean_data


@fixture
def test_raw_df():
    return pd.DataFrame(
        data=[
            "apple|2019-01-01|No|Ontario|2019-01-05|0.5|Bq/Kg|carbon".split(
                "|"
            ),
            "bread|2019-10-01|Yes|Quebec|2019-10-05|0.05|Bq/Kg|Lead-210".split(
                "|"
            ),
        ],
        columns=[
            "Food Name",
            "Sample Collection Date",
            "Human Illness Flag",
            "Sampling Location Province",
            "Analysis Completion Date",
            "Result Value",
            "Units of measurement",
            "Analyte Name",
        ],
    )


@fixture
def test_clean_df():
    return pd.DataFrame(
        data=[
            [
                "Apple Juice",
                "2002-09-15",
                "No",
                "British Columbia",
                "2003-06-15",
                0.0,
                "Bq/Kg",
                "Americium-241",
            ],
            [
                "potato chips",
                "2003-09-15",
                "No",
                "Quebec",
                "2004-06-15",
                0.0,
                "Bq/Kg",
                "Radium-226",
            ],
        ],
        columns=[
            "food_name",
            "sample_date",
            "illness",
            "province",
            "analysis_date",
            "reading",
            "units",
            "analyte",
        ],
    )


def test_clean_raw_data_handles_character_encoding():
    filename = Path(__file__).parent.joinpath("three-rows.csv")
    df = clean_raw_data(filename)
    assert set(df.columns) == set(COLUMNS.values())
    assert len(df.index) == 2


def test_clean_raw_data_produces_correct_column_names(test_raw_df):
    with patch("nitinat.data.pd.read_csv", return_value=test_raw_df):
        cooked_df = clean_raw_data("something.csv")
        assert set(cooked_df.columns) == set(COLUMNS.values())
        assert len(cooked_df.index) == len(test_raw_df.index)


def test_read_clean_data_produces_correct_columns(test_clean_df):
    structure = pd.DataFrame(
        {
            "food_name": ["something"],
            "sample_date": [np.datetime64("2022-01-01")],
            "illness": ["something"],
            "province": ["somewhere"],
            "analysis_date": [np.datetime64("2022-01-02")],
            "reading": [1.0],
            "units": ["m"],
            "analyte": ["He"],
        }
    )
    structure["province"] = pd.Categorical(structure["province"])
    with patch("nitinat.data.pd.read_csv", return_value=test_clean_df):
        final_df = read_clean_data("something.csv")
        assert all(
            final_df[c].dtype.name == structure[c].dtype.name
            for c in list(final_df)
        )
