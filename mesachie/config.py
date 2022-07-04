"""Ivy configuration file."""

# GitHub repository.
github = "https://github.com/gvwilson/mesachie/"

# Use our own theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": ["markdown.extensions.extra", "pymdownx.superfences"]
}

# Site title and subtitle.
title = "Mesachie"
tagline = "A compassionate, evidence-based introduction"
"to software engineering"

# Directories.
out_dir = "docs"

# Use "a/" URLs instead of "a.html".
extension = "/"

# Files to copy verbatim.
copy = [
    "*.py",
    "*.svg",
]

# Exclusions (don't process).
exclude = [
    "*.gz",
    "*.py",
    "*.svg",
    "*~",
]

# Chapters (slugs in order).
chapters = [
    "intro",
    "project",
    "team",
    "dstools",
]

# Appendices (slugs in order).
appendices = [
    "license",
    "conduct",
    "reviewers",
    "bib",
    "links",
    "gloss",
]

# Data files.
bibliography = "data/citations.bib"
bibliography_style = "unsrt"
glossary = "data/glossary.yml"
lang = "en"
links = "data/links.yml"
reviewers = "data/reviewers.yml"
