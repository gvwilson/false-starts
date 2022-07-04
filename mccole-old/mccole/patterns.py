"""Patterns in input."""

import re

# Comments look like HTML blocks.
COMMENT = re.compile(r"<!--\s+(.+?)\s+-->")

# Simple inline HTML.
BREAK = re.compile(r"<br/>")
CODE_OPEN = re.compile(r"<code>")
CODE_CLOSE = re.compile(r"</code>")
EM_OPEN = re.compile(r"<em>")
EM_CLOSE = re.compile(r"</em>")
STRONG_OPEN = re.compile(r"<strong>")
STRONG_CLOSE = re.compile(r"</strong>")
SUP_OPEN = re.compile(r"<sup>")
SUP_CLOSE = re.compile(r"</sup>")

# Cross-references are `<a type="key"/>`
FIGURE_REF = re.compile(r'<a\s+figure="(.+?)"\s*/>')
SECTION_REF = re.compile(r'<a\s+section="(.+?)"\s*/>')
TABLE_REF = re.compile(r'<a\s+table="(.+?)"\s*/>')

# Bibliographic citations are `<cite>key,key</cite>`.
CITE = re.compile(r"<cite>")

# Definitions are `<span g="key">text</span>` for glossary terms,
# `<span i="key">text</span>` for indexing terms,
# and `<span g="key" i="other_key">text</span>` for both.
GLOSS_REF = re.compile(r'<span\s+g="([^"]+?)">')
INDEX_DEF = re.compile(r'<span\s+i="([^"]+?)">')
GLOSS_INDEX = re.compile(r'<span\s+g="([^"]+?)"\s+i="([^"]+?)">')

# Headings with classes are `### Text {.class}`.
HEADING_CLASS = re.compile(r"\s*(.+?)(\s*\{\.(.+?)\})")

# Labeled headings are `## Text {#key}`.
HEADING_ID = re.compile(r"\s*(.+?)(\s*\{\#(.+?)\})")

# 'div' containing Markdown
DIV_CLASS_MARKDOWN = re.compile(r'<div\s+class="(.+?)"\s+markdown="1">')
DIV_CLOSE = re.compile(r'</div>')

# 'div' marking a special section
DIV_CLASS_SPECIAL = re.compile(r'<div\s+class="(.+?)"\s+special="1"\s*/>')

# Section in single-page layout.
SECTION_OPEN = re.compile(r'<section\s+id="(.+?)">')
SECTION_CLOSE = re.compile(r'</section>')

# `<div class="include" ...parameters... />`
INCLUSION = re.compile(r'<div\s+class="include"(.*?)/>')
INCLUSION_FILE = re.compile(r'^\s*file="([^"]+)"\s*$')
INCLUSION_KEEP = re.compile(r'^\s*file="([^"]+)"\s+keep="([^"]+)"\s*$')
INCLUSION_OMIT = re.compile(r'^\s*file="([^"]+)"\s+omit="([^"]+)"\s*$')
INCLUSION_KEEP_OMIT = re.compile(
    r'^\s*file="([^"]+)"\s+keep="([^"]+)"\s+omit="([^"]+)"\s*$'
)
INCLUSION_MULTI = re.compile(r'^\s*pat="([^"]+)"\s+fill="([^"]+)"\s*$')

# Line counts in source files.
LINECOUNT = re.compile(r'<span\s+class="linecount"\s+file="([^"]+)"\s*/>')

# Figures are:
# <figure id="key">
#   <img src="file" alt="short"/>
#   <figcaption>long</figcaption>
# </figure>
# The id is optional.
FIGURE = re.compile(r"<figure\b.+?</figure>", re.DOTALL)
FIGURE_ID = re.compile(r'<figure\s+id="(.+?)"\s*>\s*.+?</figure>', re.DOTALL)
FIGURE_INFO = re.compile(r'<img\s+src="(.+?)"\s+alt="(.+?)"\s*/>')
FIGURE_CAP = re.compile(r"<figcaption>(.+?)</figcaption>")

# Since there isn't a way to add an ID to a Markdown table, they are:
# <div class="table" id="key" cap="caption">
# ...Markdown table...
# </div>
TABLE_START = re.compile(r'<div.+?class="table"')
TABLE_ID = re.compile(r'id="(.+?)"')
TABLE_CAP = re.compile(r'cap="(.+?)"')
TABLE_BODY = re.compile(r"<div.+?>\n(.+)\n</div>", re.DOTALL)

# A plain '<table>' is passed through as-is (to support tables without
# header rows, multi-column items, etc.).
TABLE_RAW = re.compile(r'<table>')
