---
title: "A Minimum Viable Project"
lede: "Building a solid foundation for your work"
template: page
---

FIXME: introduction

## One Communication Channel

-   Create a mailing list for the project.
    -   The team voted 2:1 for email over Slack because they want better search and fewer interruptions.
    -   Slacks's support for threading is weak
    -   The fact that you can't easily search mailing list *and* GitHub repo is a problem

## Group Ownership

-   Create a new GitHub organization for the project and add everyone to it.
    -   So that nothing belonging to the project is under a personal account.
-   Create a new repo within that GitHub organization.
    -   Everything is in one repo for now, but that might change.
-   Note about GitLab and other forges.

## General Expectations

-   Add `README`, `LICENSE`, `CODE_OF_CONDUCT`, `GOVERNANCE`, and `.gitignore` to the repo.
    -   `README` is just a placeholder for now, but will be filled in later ([% x marketing %])


<blockquote markdown="1">
### What they really mean

In the early 2010s
some open source developers resisted the adoption of codes of conduct,
saying that they were unnecessary or that they infringed on freedom of speech.
What they actually meant
(and what the handful of people still arguing against them mean)
is that thinking about how they had benefited from unfairness in the past
made them uncomfortable.
If having a Code of Conduct makes people like that decide to join another team,
yours will be better off.
</blockquote>

## Visible Process

-   Redefine the tags in that repo.
    -   Governance: `proposal` for votable items.
    -   Issues: `bug` and `request`.
    -   Pull requests: `fix`, `enhancement`, `docs`, `testing`, and `refactor`.
    -   Meta: `question`, `paused`, `helped wanted`, `good first issue`.
    -   See [% x contributing %] for the tags used in this project.
-   Also add tags for assignments
    -   Generally a bad idea to have deadline-specific tags (they accumulate)
    -   But useful in a fixed-length course
    -   As with many practices, the answer is "it depends"

## Specific Expectations

-   Create two `pip` requirements files:
    -   `requirements.txt` is a minimal setup for using the software.
    -   `development.txt` sources that and adds everything needed for building, testing, and documenting.
-   Create `socks`, `docs`, and `tests` directories in the root of the repo along with a `setup.py` file.
    -   Pretty standard structure for a `pip`-installable Python package (and no, "socks" isn't its real name).
-   Set up `pytest` for running tests and `pdoc` for building documentation.
    -   `tests/conftest.py` for `pytest`.
    -   A docstring in every `__init__.py` file (rather than leaving it empty)
    -   Use [Google-style docstrings][google-docstrings].

## Repeatability

-   Add a `bin` directory at the top level with various utility scripts.
    -   Most of which use the code in the `socks` directory directly (rather than through a local install of the package).
-   Add a `Makefile`
    -   Or whatever
-   Add targets to `Makefile` to:
    -   Build the package.
    -   Run the tests.
    -   Run the tests with coverage and display the coverage report (to identify untested code).
    -   Rebuild the documentation.
    -   Run `flake8`, `black`, and `isort` to check that the code meets style guidelines.
-   Add a `workflow.yml` file with pre-commit checks.

## Describe and Explain

-   Used to recommend [Jekyll][jekyll] as a static site generator, since that's what GitHub supports
    -   But you probably don't speak Ruby, and setting it up is an extra burden
    -   On the other hand, setting up other static site generators is also painful
-   Pick one that works with your language and supports documentation generation
    -   [Sphinx][sphinx] for Python
    -   [ESDoc][esdoc] or [JSDoc][jsdoc] for JavaScript
    -   We use [Ivy][ivy] with a custom theme for this book since it's primarily a website, not a code project

## If You're Doing Data Science…

-   Add a `data` directory with sample data for testing and a couple of real datasets.
    -   Each dataset is in its own subdirectory with a `MANIFEST.yml` file describing files, columns, provenance, etc.
-   Add a `results` directory at the top level with one sub-directory for each paper the team intends to produce.
    -   Each sub-directory under `results` has its own `Makefile`.
    -   `make all` in the project sub-directory regenerates everything.
-   Add a `CITATION.cff` file with citation information.
    -   And make sure every contributor has an ORCID.
-   Add a BibTeX file to the root `results` directory to be used by all project papers.

## Exercises

FIXME: create exercises for this chapter.

1.  View your tickets across all repos.
1.  Use [cookiecutter][cookiecutter].
1.  Use the GitHub API to check the tags across all repos.
