---
title: Improving Testing
---

-   Data cleaning and data reading need to be tested
-   Test #1: sample actual data and read that to make sure character encoding works
    -   `head -n 3 data/canadian-dietary-radionuclides-2000-2020.csv > tests/three-rows.csv`
    -   `od -c tests/three-rows.csv` shows some non-ASCII characters

```python
from pathlib import Path
from nitinat.data import COLUMNS, clean_raw_data, read_clean_data

def test_clean_raw_data_handles_character_encoding():
    filename = Path(__file__).parent.joinpath("three-rows.csv")
    df = clean_raw_data(filename)
    assert set(df.columns) == set(COLUMNS.values())
    assert len(df.index) == 2
```

-   The special variable `__file__` holds the full path of this file
    -   Its parent is the directory that contains it
    -   So the complicated `Path` expression gets `three-rows.csv` in the current directory
-   Test #2: temporarily replace `pandas.read_csv` with something that returns a hand-written dataframe

```python
from unittest.mock import patch

def test_clean_raw_data_produces_correct_column_names(test_df):
    with patch("nitinat.data.pd.read_csv", return_value=test_df):
        cooked_df = clean_raw_data("something.csv")
        assert set(cooked_df.columns) == set(COLUMNS.values())
        assert len(cooked_df.index) == len(test_df.index)
```

-   `patch` takes the dotted path to the specific use of the function or method we want to replace
    -   And the value we want to return
    -   When `clean_raw_data` runs, `read_csv` is intercepted and our dataframe returned
-   Where does `test_df` come from?
    -   We create a fixture: a function that produces something a test can be run on

```python
@fixture
def test_df():
    return pd.DataFrame(
        data=[
            "apple|2019-01-01|No|Ontario|2019-01-05|0.5|Bq/Kg|carbon".split("|"),
            "bread|2019-10-01|Yes|Quebec|2019-10-05|0.05|Bq/Kg|Lead-210".split("|"),
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
```

-   When its name appears as a parameter to a test function, `pytest` calls our function and passes in the result
    -   It's a bit cumbersome to set up, but we can re-use `test_df` in other tests
-   How much of our code have we tested?
    -   Add a task:

```python
@task
def coverage(c):
    """Find test coverage."""
    c.run("coverage run --branch -m pytest")
    c.run("coverage html --omit='test*.py'")
```

-   [coverage][coverage] keeps track of which lines were(n't) executed and which way branches went
    -   Saves data in `.coverage` in a custom (binary) format
    -   `coverage html` generates an HTML coverage report in `htmlcov/index.html`

```
Module            statements  missing  excluded  branches  partial  coverage
nitinat/data.py           14        4         0         6        0       60%
nitinat/__init__.py        2        0         0         0        0      100%
Total                     16        4         0         6        0       64%
```

-   Clicking on `nitinat/data.py` takes us to a line-by-line report
    -   We haven't tested the data cleanup function yet
