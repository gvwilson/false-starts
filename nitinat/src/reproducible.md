---
title: Making Tasks Reproducible
---

-   Want to make common commands re-runnable
    -   More trustworthy than documentation
-   Used to use [Make][make] to do this, but it's showing its age
    -   And its syntax is unpleasant
-   Use [Invoke][invoke] instead
-   `pip install invoke` and then add `invoke>=1.7` to `requirements.txt
-   Create a file in the project's root directory called `tasks.py`:

```python
"""Run common tasks."""

from invoke import task


@task
def list(c):
    """List available tasks."""
    c.run("inv --list")


@task
def test(c):
    """Run tests."""
    c.run("pytest")
```

-   The `@task` decorator identifies functions that can be run as tasks
    -   They can do any other processing (but we don't need them to yet)
-   The `c` parameter is a context that has details about the run
    -   We don't need that yet either
-   Run `inv list`:

```
Available tasks:

  list   List available tasks
  test   Run tests
```

-   Run `inv test`: re-runs our tests
-   Get rid of the shell script and add this task to `tasks.py`:

```python
import requests


RAW_URL = "https://health.canada.ca/...2020.csv"  # URL shortened for readability
RAW_FILE = "data/canadian-dietary-radionuclides-2000-2020.csv"


@task
def get_data(c):
    """Get raw data."""
    url = RAW_URL
    response = requests.get(url)
    with open(RAW_FILE, "wb") as writer:
        writer.write(response.content)
```

-   Doing everything one way is easier to understand
-   And yes, `pip install requests` and another line in `requirements.txt`
-   If we're going to do that, add another task to clean up the data:

```python
CLEAN_FILE = "cleaned/canadian-dietary-radionuclides-2000-2020.csv"

@task
def clean_data(c):
    """Produce cleaned-up dataset."""
    df = clean_raw_data(RAW_FILE)
    df.to_csv(CLEAN_FILE)
```

-   Get rid of direct command-line execution in `nitinat/cleanup.py`
-   Note that `tasks.py` doesn't need to import `pandas`
    -   You can use an object created in another module without explicitly importing that module's dependencies
