"""Run common tasks."""

from invoke import task


@task
def build(c):
    """Build content."""
    c.run("ivy build")


@task
def coverage(c):
    """Find test coverage."""
    c.run("coverage run --branch -m pytest")
    c.run("coverage html --omit='test*.py'")


@task
def lint(c):
    """Run checks on code."""
    c.run("flake8", warn=True)
    c.run("isort --check .")
    c.run("black --check .")
    c.run("pydocstyle --convention=google --count ond")


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
def serve(c):
    """Build content and preview."""
    c.run("ivy watch")


@task
def test(c):
    """Run tests."""
    c.run("pytest")
