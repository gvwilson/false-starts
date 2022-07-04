"""Ivy configuration."""

# Site title.
title = "Software Engineering"
subtitle = "A Compassionate, Evidence-Based Approach"
acronym = "SECEBA"

# GitHub repository.
repo = "https://github.com/gvwilson/se/"

# Site logo.
logo = "codebender.svg"

# Language code.
lang = "en"

# Chapter and appendix slugs in order.
chapters = [
    "intro",
    "finale",
]
appendices = [
    "license",
    "bibliography",
    "conduct",
    "contributing",
    "glossary",
    "links",
    "credits",
    "topics",
]

# Files to copy verbatim.
copy = [
    "*.js",
    "*.png",
    "*.py",
    "*.svg",
    "*.yml",
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
    "*.yml",
    "*~",
]

# Warn about missing or unused entries.
warnings = True

# Debugging hook.
debug = False

# ----------------------------------------------------------------------

# Theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": ["markdown.extensions.extra", "pymdownx.superfences"]
}

# Output directory.
src_dir = "src"
out_dir = "docs"

# Use "a/" URLs instead of "a.html".
extension = "/"

# Links (inserted into Markdown files for consistency).
bibliography = "data/bibliography.bib"
bibliography_style = "unsrt"
glossary = "data/glossary.yml"
links = "data/links.yml"

# Footer entries are (link, title).
footer = [
    ("@root/license/", "License"),
    ("@root/conduct/", "Code of Conduct"),
    ("@root/bibliography/", "Bibliography"),
    ("@root/glossary/", "Glossary"),
    ("@root/links/", "Links"),
    (repo, "GitHub"),
]
