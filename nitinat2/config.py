"""Ivy configuration file."""

# GitHub repository.
github = "https://github.com/gvwilson/nitinat2/"

# Use our own theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": ["markdown.extensions.extra", "pymdownx.superfences"]
}

# Site title and subtitle.
title = "Nitinat"
tagline = "A model data analysis project"

# Language code.
lang = "en"

# Input and output directories.
src_dir = "src"
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
    "*.csv",
    "*.gz",
    "*.py",
    "*.svg",
    "*~",
]

# Chapters (slugs in order).
chapters = [
    "starting",
    "project",
    "dataset",
    "script",
    "unittest",
    "automation",
    "caching",
    "dependencies",
    "pipeline",
    "configuration",
    "provenance",
    "organizing",
    "documentation",
    "logging",
    "coverage",
    "packaging",
    "website",
    "indexing",
    "approximation",
    "database",
    "service",
]

# Appendices (slugs in order).
appendices = [
    "license",
    "conduct",
    "links",
    "credits",
]

# Links (inserted into Markdown files for consistency).
bibliography = "info/bibliography.bib"
bibliography_style = "unsrt"
glossary = "info/glossary.yml"
links = "info/links.yml"

# Warn about missing or unused entries.
warnings = True
