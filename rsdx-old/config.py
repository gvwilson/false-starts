"""Ark configuration file."""

title = "Research Software Design by Example"
slug = "rsdx"
website = f"https://gvwilson.github.io/{slug}/"
repo = f"https://github.com/gvwilson/{slug}"
author = "Greg Wilson"

debug = False

chapters = [
    "intro",
    "parse",
    "center",
    "script",
    "refactor",
    "test",
    "perf",
    "flow",
    "config",
    "lazy",
    "measure",
    "synth",
    "mutate",
    "site",
    "scrape",
    "query",
    "serve",
    "finale",
]

appendices = [
    "license",
    "bib",
    "conduct",
    "credits",
    "docs",
]

contents = chapters + appendices

theme = "mccole"

copy = [
    "*.png",
    "*.svg",
]

exclude = copy + [
    "*.css",
    "*.csv",
    "*.db",
    "*.dvc",
    "*.env",
    "*.metaflow",
    "*.mk",
    "*.pdf",
    "*.py",
    "*.sql",
    "*.tbl",
    "*~",
    ".#*",
    ".coverage",
    ".pytest_cache",
    "CODE_OF_CONDUCT.md",
    "DOCS.md",
    "LICENSE.md",
    "Makefile",
    "README.md",
    "__pycache__",
    "htmlcov",
    "pyproject.toml",
    "requirements.txt",
]

lint = {
    "disable_h2_id": ["conduct", "docs"],
}

markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}

src_dir = "src"
out_dir = "docs"

extension = "/"

# Display values for LaTeX generation.
if __name__ == "__main__":
    import sys

    assert len(sys.argv) == 2, "Expect exactly one argument"
    if sys.argv[1] == "--order":
        print(" ".join(contents))
    elif sys.argv[1] == "--slug":
        print(slug)
    elif sys.argv[1] == "--title":
        print(title)
    else:
        assert False, f"Unknown flag {sys.argv[1]}"
