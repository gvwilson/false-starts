"""Ivy configuration file for the Caycuse site."""

# GitHub repository.
github = "https://github.com/gvwilson/caycuse/"

# Use our own theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": ["markdown.extensions.extra", "pymdownx.superfences"]
}

# Site title and subtitle.
title = "Designing Research Software"
tagline = "An Example-Based Introduction Using Python"

# Language code.
lang = "en"

# Input and output directories.
src_dir = "src"
out_dir = "docs"

# Use "a/" URLs instead of "a.html".
extension = "/"

# Files to copy verbatim.
copy = [
    "*.png",
    "*.py",
    "*.svg",
]

# Exclusions (don't process).
exclude = [
    "*/__pycache__",
    "*/.idea",
    "*.csv",
    "*.gz",
    "*.png",
    "*.py",
    "*.pyc",
    "*.svg",
    "*.txt",
    "*~",
]

# Chapters (slugs in order).
chapters = [
    "starting",
    "scraping",
    "unittest",
    "components",
    "performance",
    "website",
]

# Appendices (slugs in order).
appendices = [
    "license",
    "conduct",
    "contributing",
    "links",
    "credits",
]

# Links (inserted into Markdown files for consistency).
bibliography = "info/bibliography.bib"
bibliography_style = "unsrt"
glossary = "info/glossary.yml"
links = "info/links.yml"

# Warn about missing or unused entries.
warnings = False
