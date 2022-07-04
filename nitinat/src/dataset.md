---
title: Handling Data
---

## Adding Data

-   Analyzing radionuclides in Canadian food from 2000 to 2020
    -   Dataset is only 12.7 Mb, which Git can handle easily
    -   But we'll pretend it's larger to illustrate a few ideas
-   Follow [Noble's Rules][nobles-rules]:
    -   A top-level directory called `data` with the raw data
    -   A `bin` directory with helper scripts, including one to download the data
    -   Belatedly add a `Setup` section to `CONTRIBUTING.md` with instructions for setting up environment and downloading data
-   The `data` directory contains:
    -   A `README.md` file describing the dataset(s)
        -   Would use something more structured (e.g., YAML) in a larger project
    -   The data dictionary we downloaded from the web
        -   Small enough to fit in Git
        -   Might copy descriptions of interesting columns to our own `README.md` as the project progresses
    -   A `.gitignore` to make sure the dataset isn't saved in Git

## Cleaning Data

-   We have raw data, but need a cleaned dataset for further analysis
-   Install `pandas` using `pip install pandas`
    -   And add `pandas>=1.4` to `requirements.txt`
-   Add `nitinat/cleanup.py` to hold data cleaning utilities
-   Initial content:

```python
"""Handle details of particular datasets."""

import pandas as pd


def clean_raw_data(filename):
    """Extract subset of interest from raw data."""
    return pd.read_csv(filename)


if __name__ == "__main__":
    import sys
    df = clean_raw_data(sys.argv[1])
    print(df.info())
```

-   Every file starts with a docstring, followed by package imports
    -   Everything we want to re-use goes in a function
    -   For interactive testing during development we will load a file specified on the command line
-   It doesn't work:

```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 705: invalid continuation byte
```

-   Character set encoding problem
-   Try specifying `encoding="utf-8"` explicitly: no effect
-   Search for "what character set does Excel use when saving files?"
    -   Tabular data...
-   Eventually wind up with:

```python
EXCEL_ENCODING = "Windows-1252"

def clean_raw_data(filename):
    """Extract subset of interest from raw data."""
    df = pd.read_csv(filename, encoding=EXCEL_ENCODING)
    return df
```

-   This is why we write cleanup code...
-   Now add code to select the columns we care about and saved the result
    -   Choose columns by inspection
    -   Rename them for less typing
    -   Save as `cleaned/canadian-dietary-radionuclides-2000-2020.csv`
    -   60 kb instead of 12 Mb, so we can save it in Git
    -   Still specifying source and destination on the command line: need to fix that
