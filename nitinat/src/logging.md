---
title: Logging
---

-   Please use an interactive debugger rather than `print` statements when you're developing or debugging
-   But please also add some logging to any code that's going into production
    -   Like `print`, but the level of detail and the destination can be configured without changing the code
-   Python's `logging` library takes a few steps to set up in `__init__.py`:

```python
import logging
import time

CONFIG = {
    "LOGGER": None,
    "LOGGING_NAME": "Nitinat",
    "LOGGING_LEVEL": "warn",
}

def get_logger():
    """Get the logger used by this module."""
    if CONFIG["LOGGER"] is None:
        name = CONFIG["LOGGING_NAME"]
        logger = logging.getLogger(name)
        logger.setLevel(CONFIG["LOGGING_LEVEL"].upper())
        formatter = logging.Formatter(
            fmt=f"{name} %(asctime)s %(message)s",
            datefmt="%y-%m-%d:%H:%M:%S",
        )
        formatter.converter = time.gmtime
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        CONFIG["LOGGER"] = logger
    return CONFIG["LOGGER"]
```

-   We store configuration values in `CONFIG` (which we can use to configure other parts of the module too)
    -   The logger is initially `None`: we'll create it on demand the first time it's needed and recycle after that
        -   A [singleton][singleton]
    -   We give the logger a name to distinguish its messages from those produced by other modules
    -   And we specify the default level of detail (choices are `DEBUG`, `INFO`, `WARN`, `ERROR`, and `CRITICAL`)
    -   When we create the logger, we specify the level, the format of messages, and that we want messages to standard error
-   Our data-cleaning function now looks like:

```python
def clean_raw_data(filename):
    """Extract subset of interest from raw data."""
    logger = get_logger()
    df = pd.read_csv(filename, encoding=EXCEL_ENCODING)
    df = df[[col for col in COLUMNS.keys()]]
    df.rename(columns=COLUMNS, inplace=True)
    logger.info(f"clean {filename}: {len(df.columns)} columns x {len(df.index)} rows")
    return df
```

-   Get the logger
    -   Report a message at `INFO` level
-   And we change `tasks.py` to:

```python
@task(optional=["logging"])
def clean_data(c, logging=None):
    """Produce cleaned-up dataset."""
    _configure_logging(logging)
    df = clean_raw_data(RAW_FILE)
    df.to_csv(CLEAN_FILE)


def _configure_logging(log_level):
    """Initialize logging."""
    if log_level is not None:
        CONFIG["LOGGING_LEVEL"] = log_level.upper()
```

-   The `optional` argument to `@task` tells [Invoke][invoke] that this task takes a `--logging=NAME` command-line option
-   If that option is provided, we re-set the logging level
    -   We don't re-create the logger when this happens, which is either a bug or a feature
-   Let's try running it:

```bash
$ inv clean-data
# no output
$ inv clean-data --logging=info
Nitinat 22-03-23:15:12:45 clean data/canadian-dietary-radionuclides-2000-2020.csv: 8 columns x 18698 rows
```

-   With a bit more work we can put the logging configuration in a configuration file to make it even easier
