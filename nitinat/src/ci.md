---
title: Continuous Integration
---

-   Should always run checks when committing code
    -   Or changing documentation, or...
-   But human beings are fallible, so automate: continuous integration (CI)
-   Many dedicated CI services like [Circle CI][circle-ci]
-   For a project this size, easiest is [GitHub Actions][gh-actions]
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
    -   Use a [pre-defined `checkout` action][gh-actions-predefined] to get a fresh copy of the repo
    -   Set up Python using another pre-defined action
    -   Install everything listed in `requirements.txt`
    -   Run the code checks (do *not* reformat, just check)
    -   Run the tests: the `if` condition means "even if the previous linting step fails"
-   Before we test it, let's split requirements into "needed for install" and "also used in dev"
-   `requirements.txt` becomes:

```
kaleido>=0.2
pandas>=1.4
plotly>=5.6
pydantic>=1.9.0
pyyaml>=5.4
requests>=2.27
statsmodels>=0.13
```

-   Create a new file `development.txt` that tells `pip` to read `requirements.txt` (using `-r`) then add more packages

```
-r requirements.txt
black>=22.1
coverage>=6.3
flake8>=4.0
invoke>=1.7
isort>=5.10
ivy>=6.2
pdoc3>=0.10
pymdown-extensions>=9.3
pyproject-flake8
pytest>=7.1
```

-   `git add` changes, commit, push to GitHub, go to the `Actions` tab: the job has failed
    -   Because `invoke` isn't included in `requirements.txt`, but is needed for the action
    -   So are `black`, `flake8`, `isort`, and `pytest`
-   Move `invoke` to `requirements.txt`, add, commit, push
    -   Works this time
    -   Some projects have `development.txt`, `testing.txt`, and `requirements.txt` for this reason
    -   It all should live in `pyproject.toml`...

<div class="callout" markdown="1">
### Other Jobs

The GitHub Actions tab shows all the jobs, including the ones that build and deploy the website.
If you have pushed several times, then rebase and push the combined commit,
the jobs run by the now-squashed commits still show up.
</div>
