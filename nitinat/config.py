"""Ivy configuration file."""

# GitHub repository.
github = "https://github.com/gvwilson/nitinat/"

# Use our own theme.
theme = "nitinat"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": ["markdown.extensions.extra", "pymdownx.superfences"]
}

# Site title and subtitle.
title = "Nitinat"
tagline = "A model data analysis project in Python"

# Input and output directories.
src_dir = "src"
out_dir = "docs"

# Resources directory (use all results).
res_dir = "results"

# Links (inserted into Markdown files for consistency).
links = "links.yml"

# Chapters (slugs in order).
chapters = [
    "starting",
    "project",
    "dataset",
    "reproducible",
    "results",
    "quality",
    "setback-01",
    "configuration",
    "testing",
    "logging",
    "technical-debt-01",
    "parameters",
    "pipeline-01",
    "technical-debt-02",
    "pipeline-02",
    "website-01",
    "pipeline-03",
    "website-02",
    "documentation",
    "packaging",
    "ci",
    "indexing",
    "dependencies",
    "layered",
    "database",
]

# Appendices (slugs in order).
appendices = [
    "data",
    "license",
    "links",
    "credits",
]

# Dataset pattern, template, and output directory
data = {
    "out_dir": "data",
    "src_glob": "parameters/*.json",
    "template": "datapage.html",
}
