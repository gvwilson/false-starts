"""Ivy configuration file."""

# ----------------------------------------

# Abbreviation for this document.
abbrev = "seceba"

# GitHub repository.
github = "https://github.com/gvwilson/seceba"

# Site title and subtitle.
title = "The Compassionate Programmer"
acronym = "TCP"
tagline = "evidence - process - tools"
author = "Greg Wilson"

# Chapters.
chapters = [
    "introduction",
    "teamwork",
    "tooling",
    "communication",
    "process",
    "pipeline",
    "devops",
    "roles",
    "testing",
    "design",
    "performance",
    "rights",
    "responsibilities",
    "conclusion",
]

# Appendices (slugs in order).
appendices = [
    "bibliography",
    "syllabus",
    "license",
    "conduct",
    "tips",
    "checklists",
    "glossary",
    "links",
    "credits",
    "contents",
]

# Debug.
debug = True

# Warn about missing or unused entries.
warnings = True

# ----------------------------------------

# Use our own theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": ["markdown.extensions.extra", "pymdownx.superfences"]
}

# External files.
acknowledgments = "info/acknowledgments.yml"
bibliography = "info/bibliography.bib"
bibliography_style = "unsrt"
credits = "info/credits.yml"
glossary = "info/glossary.yml"
links = "info/links.yml"

# Language code.
lang = "en"

# Input and output directories.
src_dir = "src"
out_dir = "docs"

# Use "a/" URLs instead of "a.html".
extension = "/"

# Files to copy verbatim.
copy = [
    "*.html",
    "*.pdf",
    "*.png",
    "*.py",
    "*.svg",
]

# Exclusions (don't process).
exclude = [
    "*/MANIFEST.yml",
    "*.csv",
    "*.gz",
    "*.mk",
    "*.out",
    "*.pdf",
    "*.png",
    "*.py",
    "*.pyc",
    "*.svg",
    "*.txt",
    "*~",
    "*/__pycache__",
]

# Display values for LaTeX generation.
if __name__ == "__main__":
    import sys

    assert len(sys.argv) == 2, "Expect exactly one argument"
    if sys.argv[1] == "--abbrev":
        print(abbrev)
    elif sys.argv[1] == "--latex":
        print(f"\\title{{{title}}}")
        print(f"\\subtitle{{{tagline}}}")
        print(f"\\author{{{author}}}")
    elif sys.argv[1] == "--tagline":
        print(tagline)
    elif sys.argv[1] == "--title":
        print(title)
    else:
        assert False, f"Unknown flag {sys.argv[1]}"
