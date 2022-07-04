---
title: Technical Debt Revisited
---

-   We haven't run `inv reformat` for a while
-   And we shouldn't be using `setup.cfg` these days: modern Python uses `pyproject.toml` for configuration
-   `git mv setup.cfg pyproject.toml` (so we don't lose history)
-   Run `inv lint`: lots of warnings
-   Run `inv reformat` to fix some of them automatically, then `inv lint` again
    -   `flake8` complains about line lengths
    -   Because it doesn't (yet) read from `pyproject.toml`
    -   So install [pyproject-flake8][pyproject-flake8] and change `flake8` to `pflake8` in `tasks.py`
-   Fix complaints and commit
