---
title: The First Setback
---

-   Want to add two more plots:
    -   Histogram of analyses by analyte
    -   Scatter plot of analysis date vs. sample date, with trend line
-   The first is easy:
    -   Add function to `nitinat/plotting.py`
    -   Add entry to `PLOTS` dictionary in `tasks.py`
-   Start the second with a simple scatter plot (no trend line)

```python
def sample_vs_analysis_date(datafile, plotfile):
    """Create scatter plot of sample and analysis dates."""
    df = read_clean_data(datafile)
    fig = px.scatter(df, x="sample_date", y="analysis_date")
    fig.write_image(plotfile)
```

-   No problem
-   Then add a trendline as per the documentation

```python
def sample_vs_analysis_date(datafile, plotfile):
    """Create scatter plot of sample and analysis dates."""
    df = read_clean_data(datafile)
    fig = px.scatter(df, x="sample_date", y="analysis_date",
                     trendline="ols")
    fig.write_image(plotfile)
```

-   To cut a long story short:
    -   Need the [statsmodels][statsmodels] package to create trendlines
    -   It needs [BLAS][blas], which is compiled (non-Python) code
    -   `pip install statsmodels` doesn't work
    -   After several failures, use `conda install -c anaconda statsmodels`
    -   Which means an important dependency won't be in our `requirements.txt` file
    -   Which means it's time to switch to conda for installation
    -   File an issue...
-   But creating a trendline still fails
    -   The `sample_date` and `analysis_date` columns in the dataframe are strings, not datetimes
-   Modify `read_clean_data`:

```python
DATE_FORMAT = "%Y-%m-%d"

def read_clean_data(filename):
    """Read cleaned-up data."""
    df = pd.read_csv(filename)
    province_cat = [p[0] for p in PROVINCES]
    df["province"] = pd.Categorical(df["province"], province_cat, ordered=True)\
                       .rename_categories({p[0]: p[1] for p in PROVINCES})
    for column in ("sample_date", "analysis_date"):
        df[column] = pd.to_datetime(df[column], format=DATE_FORMAT)
    return df
```

-   But it *still* doesn't work

```
numpy.core._exceptions._UFuncBinaryResolutionError: \
ufunc 'subtract' cannot use operands with types dtype('<M8[ns]') and dtype('O')
```

-   A [duck search][duckduckgo] says that:
    -   `dtype('<M8[ns]')` is a specific kind of 64-bit datetime (OK)
    -   `dtype('O')` is...a generic Python object, such as a string
-   File an issue and move on
-   Then install [GitHub command-line client][gh-cmdline], authorize, and use `gh issue list`:

```
#3  Cannot add trendline to plot of sample date vs. analysis date  problem  less than a minute ago
#2  Replace requirements.txt with conda installation file          request  about 30 minutes ago
```

-   Reduces friction for small operations
-   `git log` is where the project has been; `gh issue list` is where it's going
