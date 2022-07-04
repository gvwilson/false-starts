---
title: Checking Code Quality
---

-   [PEP 8][pep8] lays out some guidelines for readable Python, but checking those rules is tedious
-   [Black][black], [Flake8][flake8], and [isort][isort] check most of the rules for you
    -   And can reformat code to obey them
-   `pip install black flake8 isort` and then add entries to `requirements.txt`
-   `black --check .` will check all the Python code in or below the current directory
-   `black .` will reformat anything that doesn't conform to style guidelines
-   `flake8` only checks for flaky code
-   `isort` can both check and reformat (order and format of `import` statements)
-   So add two tasks to `tasks.py`:
    -   The term "lint" comes from an early tool for C that reported questionable code

```python
@task
def lint(c):
    """Run checks on code."""
    c.run("flake8", warn=True)
    c.run("isort --check .")
    c.run("black --check .")


@task
def reformat(c):
    """Reformat code."""
    c.run("isort .")
    c.run("black .")
```

-   `inv lint` produces:

```
./tests/test_heartbeat.py:3:1: F401 'nitinat' imported but unused
ERROR: /u/nitinat/tasks.py Imports are incorrectly sorted and/or formatted
ERROR: /u/nitinat/nitinat/plotting.py Imports are incorrectly sorted and/or formatted
ERROR: /u/nitinat/nitinat/data.py Imports are incorrectly sorted and/or formatted
Skipped 1 files
```

-   `inv reformat` makes minor changes, e.g. replaces:

```python
fig = px.histogram(df, x="province",
                   category_orders={"province": df["province"].cat.categories})
```

-   with:

```python
fig = px.histogram(
    df, x="province", category_orders={"province": df["province"].cat.categories}
)
```

-   Prefer the first, but consistency makes things more readable [[Hermans2021][programmers-brain]]
-   And change the heartbeat test to actually use the `nitinat` module:

```python
def test_module_can_be_imported():
    assert hasattr(nitinat, "__author__")
    assert hasattr(nitinat, "__version__")
```
