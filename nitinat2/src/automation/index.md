---
title: "Automation"
---

-   Want to make common commands re-runnable
    -   More trustworthy than documentation
-   Many (many) [% g build_tool "build automation tools" %] to do this
    -   Called that because the first one was invented to recompile (build) C programs
-   [Make][make] is the original and still most widely used, but its syntax is unpleasant
-   [Snakemake][snakemake] can do a lot [% b Molder2021 %], but it is also complicated
-   Use [Invoke][invoke] instead
-   `pip install invoke` and then add `invoke>=1.7` to `requirements.txt
-   Create a file in the project's root directory called `tasks.py`:

```{.python title="tasks.py"}
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

-   The `@task` [% g decorator "decorator" %] identifies functions that can be run as tasks
    -   They can do any other processing (but we don't need them to yet)
-   The `c` parameter is a context that has details about the run
    -   We don't need that yet either
-   Run `inv list`:

```text
Available tasks:

  list   List available tasks
  test   Run tests
```

-   [PEP 8][pep8] lays out some guidelines for readable Python, but checking those rules is tedious
-   [Black][black], [Flake8][flake8], and [isort][isort] check most of the rules for you
    -   And can reformat code to obey them
-   These tools are called [% g linter "linters" %]
    -   Because the first one (called `lint`) warned about fluff in C programs
-   `pip install black flake8 isort` and then add entries to `requirements.txt`
-   `black --check .` will check all the Python code in or below the current directory
-   `black .` will reformat anything that doesn't conform to style guidelines
-   isort can both check and reformat (order and format of `import` statements)
-   flake8 only checks for flaky code
-   So add two tasks to `tasks.py`:
    -   The term "lint" comes from an early tool for C that reported questionable code

```{.python title="tasks.py"}
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
./nitinat/download.py:68:80: E501 line too long (81 > 79 characters)
./nitinat/download.py:78:35: F541 f-string is missing placeholders
./tests/test_download.py:60:46: E711 comparison to None should be 'if cond is None:'
./tests/test_heartbeat.py:3:1: F401 'nitinat' imported but unused
```

-   The second problem comes from this line:

```{.python title="nitinat/download.py"}
assert isinstance(arg, dict), f"Expected int or dict"
```

-   A [% g f_string "format string" %] that isn't formatting anything
    -   Easy to fix
-   Change the comparison in the test
-   And change the heartbeat test to:

```{.python title="tests/test_heartbeat"}
def test_module_can_be_imported():
    assert hasattr(nitinat, "__author__")
    assert hasattr(nitinat, "__version__")
```

-   The first problem in the list is a line that's one character too long:

```python
parser.add_argument("--verbose", action="store_true", help="Report progress")
```

-   Unfortunately, black and flake8 disagree on how long lines should be
-   So create `setup.cfg` in the root directory of the project

```
[flake8]
max-line-length = 88

[isort]
profile = black
multi_line_output = 3

[tool:pytest]
addopts = -rfE -q
```

-   Tell flake8 to use 88-character lines (which is black's default)
-   Tell isort to match black's preferred import order
    -   And to use [vertical hanging indent for multi-line output][isort_config]
-   While we're here, tell pytest to produce a little less output
-   Should always run checks when committing code
    -   Or changing documentation, or...
-   But human beings are fallible, so automate: continuous integration (CI)
-   Many dedicated CI services like [Circle CI][circle_ci]
-   For a project this size, easiest is [GitHub Actions][gh_actions]
-   Create a directory `.github/workflows` beneath the root of the project
-   Add a file `test-on-push.yml` in that directory:

```yaml
name: Test on Push
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v1
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run code checks
        run: inv lint
      - name: Run tests
        run: inv test
        if: ${{ always() }}
```

-   `name` is the name of the action (used in error reporting, etc.)
-   `on` defines when the action runs
    -   When there's a `push` to the `main` branch
    -   When anyone creates a pull request whose target is `main`
    -   Lots of other options
-   `jobs` defines what to do when the action runs
    -   An action can run many jobs in parallel
-   We want to build our software on the latest version of Ubuntu Linux
    -   Probably the most common platform
-   Spell out the steps:
    -   Use a [pre-defined `checkout` action][gh_actions_predefined] to get a fresh copy of the repo
    -   Set up Python using another pre-defined action
    -   Install everything listed in `requirements.txt`
    -   Run the code checks (do *not* reformat, just check)
    -   Run the tests: the `if` condition means "even if the previous linting step fails"
-   `git add` changes, commit, push to GitHub, go to the `Actions` tab
