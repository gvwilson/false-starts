"""Run common tasks."""

import os
from pathlib import Path

import requests
from invoke import task
from pyinvokedepends import depends

from nitinat import CONFIG
from nitinat.data import clean_raw_data
from nitinat.plotting import (
    count_by_analyte,
    count_by_province,
    sample_vs_analysis_date,
)

RAW_URL = "https://health.canada.ca/apps/open-data/stud-etud-diet-alim-total/"
"radion/Total%20Diet%20Study%20Radionuclides%20results%202000-2020.csv"
RAW_FILE = "data/canadian-dietary-radionuclides-2000-2020.csv"
CLEAN_FILE = "cleaned/canadian-dietary-radionuclides-2000-2020.csv"
RESULTS_DIR = "results"
PLOTS = {
    "count_by_analyte": count_by_analyte,
    "count_by_province": count_by_province,
    "sample_vs_analysis_date": sample_vs_analysis_date,
}
PLOT_TYPE = ".svg"
LOG_FORMAT = "Nitinat (%(asctime)s) %(message)s"


@task(optional=["level"])
def logging(c, level=None):
    if level is not None:
        CONFIG["LOGGING_LEVEL"] = level.upper()


@depends(on=[RAW_FILE], creates=[CLEAN_FILE])
@task(pre=[logging])
def clean_data(c):
    """Produce cleaned-up dataset."""
    df = clean_raw_data(RAW_FILE)
    df.to_csv(CLEAN_FILE, index=False)


@task
def coverage(c):
    """Find test coverage."""
    c.run("coverage run --branch -m pytest")
    c.run("coverage html --omit='test*.py'")


@task
def get_data(c):
    """Get raw data."""
    url = RAW_URL
    response = requests.get(url)
    with open(RAW_FILE, "wb") as writer:
        writer.write(response.content)


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


@task
def lint(c):
    """Run checks on code."""
    c.run("pflake8", warn=True)
    c.run("isort --check .")
    c.run("black --check .")


@task
def list(c):
    """List available tasks."""
    c.run("inv --list")


@task
def reformat(c):
    """Reformat code."""
    c.run("isort .")
    c.run("black .")


@task
def test(c):
    """Run tests."""
    c.run("pytest")


@task
def website(c):
    """Build website."""
    from config import out_dir

    c.run("ivy build")
    c.run(f"pdoc --html --force --output-dir {out_dir} nitinat")


def _out_of_date(target, *dependencies):
    """Check if something is out of date."""
    if not os.path.exists(target):
        return True
    return os.path.getmtime(target) <= max(
        os.path.getmtime(d) for d in dependencies
    )
