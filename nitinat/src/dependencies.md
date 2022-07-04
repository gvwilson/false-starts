---
title: Handling Task Dependencies
---

-   Consider this simple Makefile:

```make
RAW_FILE = "data/canadian-dietary-radionuclides-2000-2020.csv"
CLEAN_FILE = "cleaned/canadian-dietary-radionuclides-2000-2020.csv"
PLOT_FILE = "results/count_by_analyte.svg"

${CLEAN_FILE}: ${RAW_FILE}
        python clean_data.py < ${RAW_FILE} > ${CLEAN_FILE}

${PLOT_FILE}: ${CLEAN_FILE}
        python plot_histogram.py < ${CLEAN_FILE} > ${PLOT_FILE}
```

-   If the raw data file is newer than the cleaned-up data file, Make re-cleans the data
-   And if the cleaned-up data file is newer than the plot file, Make re-creates the plot
-   If the plot is out of date with respect to the raw data, both steps happen automatically in the right order
-   We can make [Invoke][invoke] tasks depend on each other
-   Reminder: we have these definitions at the top of `tasks.py`:

```python
RESULTS_DIR = "results"
PLOTS = {
    "count_by_analyte": count_by_analyte,
    "count_by_province": count_by_province,
    "sample_vs_analysis_date": sample_vs_analysis_date,
}
PLOT_TYPE = ".svg"
```

-   So we use the `pre` keyword to the `@task` decorator applied to `plot_data`
    -   Takes a list of other task functions
    -   Any task will be executed at most once

```python
@task(optional=["logging"])
def clean_data(c, logging=None):
    """Produce cleaned-up dataset."""
    _configure_logging(logging)
    df = clean_raw_data(RAW_FILE)
    df.to_csv(CLEAN_FILE, index=False)

@task(pre=[clean_data], optional=["logging"])
def plot_data(c, logging=None):
    """Create plots of data."""
    _configure_logging(logging)
    for stem in PLOTS:
        result = Path(RESULTS_DIR, stem).with_suffix(PLOT_TYPE)
        PLOTS[stem](CLEAN_FILE, str(result))
```

-   But this always re-runs `clean_data` when we ask for `inv plot_data`
-   There is an extension called [pyinvokedepends][py-invoke-depends] that enables us to specify dependencies between files
-   But it doesn't play nicely with optional arguments (like `logging`)
-   Option 1: do away with logging
-   Option 2: do it ourself

```python
@task(optional=["logging"])
def clean_data(c, logging=None):
    """Produce cleaned-up dataset."""
    _configure_logging(logging)
    if _out_of_date(CLEAN_FILE, RAW_FILE):
        df = clean_raw_data(RAW_FILE)
        df.to_csv(CLEAN_FILE, index=False)


def _out_of_date(target, *dependencies):
    """Check if something is out of date."""
    if not os.path.exists(target):
        return True
    return os.path.getmtime(target) <= max(
        os.path.getmtime(d) for d in dependencies
    )
```

-   This does the right thing, and can easily be extended to multi-file dependencies
-   But the next person to work with the code will have to read the body of each task function to see what depends on what
-   And we still have problems with the `logging` optional argument
    -   It is only passed to the top-level task we invoke, not to sub-tasks
    -   So if we run `inv plot-data --logging debug`, we only get logging from `plot_task`, not from `clean_data`
    -   Which is misleading
-   So take another approach: make logging a task and have other tasks depend on it

```python
@task(optional=["level"])
def logging(c, level=None):
    if level is not None:
        CONFIG["LOGGING_LEVEL"] = level.upper()

@task(pre=[logging])
def clean_data(c):
    """Produce cleaned-up dataset."""
    if _out_of_date(CLEAN_FILE, RAW_FILE):
        df = clean_raw_data(RAW_FILE)
        df.to_csv(CLEAN_FILE, index=False)


@task(pre=[logging, clean_data])
def plot_data(c):
    """Create plots of data."""
    for stem in PLOTS:
        result = Path(RESULTS_DIR, stem).with_suffix(PLOT_TYPE)
        if _out_of_date(result, CLEAN_FILE):
            PLOTS[stem](CLEAN_FILE, str(result))
```

-   The command line is then:

```shell
$ touch data/canadian-dietary-radionuclides-2000-2020.csv 
$ inv logging --level info plot-data
Nitinat 22-04-02:14:38:44 clean data/canadian-dietary-radionuclides-2000-2020.csv: 8 columns x 18698 rows
Nitinat 22-04-02:14:38:44 read cleaned/canadian-dietary-radionuclides-2000-2020.csv: 8 columns x 18698 rows
Nitinat 22-04-02:14:38:45 read cleaned/canadian-dietary-radionuclides-2000-2020.csv: 8 columns x 18698 rows
Nitinat 22-04-02:14:38:45 read cleaned/canadian-dietary-radionuclides-2000-2020.csv: 8 columns x 18698 rows
$ inv logging --level info plot-data
#> no output
```

-   Now go back and try [pyinvokedepends][py-invoke-depends] again

```
@depends(on=[RAW_FILE], creates=[CLEAN_FILE])
@task(pre=[logging])
def clean_data(c):
    """Produce cleaned-up dataset."""
    df = clean_raw_data(RAW_FILE)
    df.to_csv(CLEAN_FILE, index=False)
```

-   Works when the raw file is newer than the cleaned file

```shell
$ touch data/canadian-dietary-radionuclides-2000-2020.csv 
$ inv logging --level info clean-data
Nitinat 22-04-02:14:43:50 clean data/canadian-dietary-radionuclides-2000-2020.csv: 8 columns x 18698 rows
```

-   Still works when the cleaned file is newer

```shell
$ inv logging --level info clean-data
Not calling clean_data
```

-   Plotting is only a little more complicated to set up
    -   Have to define `_make_plot_file` *before* using it because the decorator is executed as the code loads

```python
def _make_plot_file(stem):
    """Make a plot filename."""
    return Path(RESULTS_DIR, stem).with_suffix(PLOT_TYPE)


@depends(on=[CLEAN_FILE], creates=[_make_plot_file(stem) for stem in PLOTS])
@task(pre=[logging, clean_data])
def plot_data(c):
    """Create plots of data."""
    for stem in PLOTS:
        result = _make_plot_file(stem)
        if _out_of_date(result, CLEAN_FILE):
            PLOTS[stem](CLEAN_FILE, str(result))
```

-   File bug reports with [pyinvokedepends][py-invoke-depends-bug] and [invoke][invoke-bug]
-   And [ask a question][invoke-so-question] on [Stack Overflow][stack-overflow]
-   Doing this is part of being a good open source community member
