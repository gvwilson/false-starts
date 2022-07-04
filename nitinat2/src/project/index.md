---
title: Setting Up a Python Project
---

-   Organize files as if every project was going to become a package
    -   Because it might
    -   And it means things are in predictable places
-   Create `nitinat` directory to contain package code
    -   Standard Python package structure to keep package code separate from support code
    -   Pronounced "nit-nat": it's a small town near where the author grew up
-   Add `nitinat/__init__.py`:

```{.python title="nitinat/__init__.py"}
"""Nitinat: a model data analysis project in Python."""

__version__ = "0.1.0"
__author__ = "Greg Wilson"
```

-   The existence of `__init__.py` signals that this directory is an importable module
    -   It can even be empty
-   First line is a documentation string (docstring) explaining the file's purpose
-   The `__version__` and `__author__` variables are recognized by Python's packaging tools
-   Create `tests` directory *beside* the `nitinat` package directory to contain tests
    -   And create `tests/__init__.py` to keep testing tools happy

```{.python title="tests/__init__.py"}
"""Make tests look like a module so actual module will load."""
```

-   Create a [conda][conda] virtual environment to avoid conflicts between packages installed for different projects
    -   Some people prefer [Docker][docker] for isolating environments,
        and because it's what we'll eventually use when we run in the cloud

```bash
$ conda create -n nitinat python=3.9
# say 'y' to the prompt
$ conda activate nitinat
```

-   Install [pytest][pytest] to run tests:
    -   Can use `conda install`, but `pip` is simpler for small projects
    -   Can also install [mamba][mamba] and use `mamba install`, which is faster for complicated setups

```bash
$ pip install pytest
```

-   Create `requirements.txt` to make package installation reproducible
    -   What version did we get?

```bash
$ conda list pytest
# Name                    Version                   Build  Channel
pytest                    7.1.1                    pypi_0    pypi
```

-   Use three-part [semantic versioning][semver] to identify major version, minor version, and patch
-   Create `requirements.txt` file with major and minor version

```{.txt title="requirements.txt"}
pytest>=7.1
```

-   Create a "heartbeat" test in `tests/test_heartbeat.py` to make sure we can load our module

```{.python title="tests/test_heartbeat.py"}
"""Check that the project has a heartbeat."""

import nitinat


def test_module_can_be_imported():
    pass
```

-   Names of test files and functions must started with `test_` so that `pytest` can find them
    -   Don't use docstrings for tests: give them long informative names
    -   This test doesn't check anything (`pass`), but `pytest` will complain if `nitinat` cannot be imported
-   Run the test:

```bash
$ pytest
#> collected 1 item
#> tests/test_heartbeat.py .  
```

-   Add to these notes, commit, and push
