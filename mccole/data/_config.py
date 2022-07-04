"""Ivy configuration."""

# Site title.
title = "Your Title Goes Here"
subtitle = "Your Subtitle Goes Here"

# GitHub repository.
repo = "https://github.com/someone/something/"

# Site logo.
logo = "codebender.svg"

# Language code.
lang = "en"

# Chapter and appendix slugs in order.
chapters = []
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

# Warn about missing or unused entries.
warnings = False

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
