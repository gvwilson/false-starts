"""Ivy configuration file."""

# Theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {"extensions": ["markdown.extensions.extra", "markdown.extensions.codehilite"]}

# Site title.
title = "Software Engineering"
subtitle = "A Compassionate, Evidence-Based Approach"

# Output directory.
out_dir = "docs"

# GitHub repository.
github = "https://github.com/gvwilson/seceba"

# Published domain.
domain = "buildtogether.tech"

# Site logo.
logo = "codebender.svg"

# Use "a/" URLs instead of "a.html".
extension = "/"

# Language code.
lang = "en"

# Chapter and appendix slugs in order.
chapters = [
    "intro",
    "mvp",
    "dstools",
    "analysis",
    "significance",
    "coordinate",
]
appendices = [
    "license",
    "conduct",
    "contributing",
    "governance",
    "thinking",
    "bibliography",
    "glossary",
    "links",
    "authors",
    "colophon"
]
old = [
    "meetings",
    "mvp",
    "teams",
    "conflict",
    "git",
    "review",
    "process",
    "automation",
    "design",
    "marketing",
    "eval-individual",
]

# Show warnings during build?
warnings = False

# BibTeX bibliography file and style.
bibliography = "data/bibliography.bib"
bibliography_style = "unsrt"

# Glossary definitions.
glossary = "data/glossary.yml"

# Link table file.
links = "data/links.yml"

# Reviewers table file.
reviewers = "data/reviewers.yml"

# Footer entries are (link, title).
footer = [
    ("@root/license/", "License"),
    ("@root/conduct/", "Code of Conduct"),
    ("@root/bibliography/", "Bibliography"),
    ("@root/glossary/", "Glossary"),
    ("@root/links/", "Links"),
    (github, "GitHub"),
]
