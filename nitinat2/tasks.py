"""Run common tasks."""

from invoke import task


@task
def lint(c):
    """Run checks on code."""
    c.run("flake8", warn=True)
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
