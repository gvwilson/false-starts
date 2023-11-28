"""Utilities for building site."""

import markdown
from pathlib import Path
import pybtex.database
import pybtex.plugin
import re
import sys
import yaml

import ark


# Constants.
BIB_STYLE = "unsrt"
DIRECTIVES_FILE = ".ark"

# Level-1 Markdown heading.
FIRST_H1 = re.compile(r"^#\s+.+$", re.MULTILINE)

# Match inside HTML paragraph markers.
INSIDE_PARAGRAPH = re.compile(r"<p>(.+?)</p>")

# Match a reference to a footer link or a URL ref in an index entry.
MARKDOWN_FOOTER_LINK = re.compile(r"\[.*?\]\[(.+?)\]", re.MULTILINE)


def debug(msg):
    """Report if debugging turned on."""
    if ark.site.config.get("debug", False):
        print(msg)


def fail(msg):
    """Fail unilaterally."""
    print(msg, file=sys.stderr)
    sys.exit(1)


def get_slug(node):
    """Get chapter-level slug of file."""
    if len(node.path) == 0:
        return ""
    if node.path[-1] == "slides":
        return node.path[-2]
    return node.path[-1]


def get_tag(node):
    """Get chapter tag from collected page metadata."""
    slug = get_slug(node)
    require((slug in ark.site.config["_meta_"]), f"{node} not known")
    return ark.site.config["_meta_"][slug].get("tag", None)


def get_title(node):
    """Get chapter/appendix title from collected page metadata."""
    slug = get_slug(node)
    require((slug in ark.site.config["_meta_"]), f"{node} not known")
    return ark.site.config["_meta_"][slug]["title"]


def markdownify(text, strip_p=False):
    """Convert Markdown to HTML."""
    extensions = ["markdown.extensions.extra", "markdown.extensions.smarty"]
    combined = f"{text}\n{ark.site.config['_links_block_']}"
    result = markdown.markdown(combined, extensions=extensions)
    if strip_p and result.startswith("<p>"):
        result = INSIDE_PARAGRAPH.match(result).group(1)
    return result


def read_bibliography():
    """Load bibliography."""
    filename = Path(ark.site.home(), "info", "bibliography.bib")
    try:
        raw = pybtex.database.parse_file(filename)
        style_name = ark.site.config.get(BIB_STYLE, None)
        style = pybtex.plugin.find_plugin("pybtex.style.formatting", style_name)()
        styled_bib = style.format_bibliography(raw)
        return styled_bib
    except FileNotFoundError:
        fail(f"Unable to read bibliography {filename}")
    except pybtex.exceptions.PybtexError:
        fail(f"Unable to parse bibliography {filename}")


def read_directives(dirname):
    """Get contents of directives file if it exists"""
    filepath = Path(dirname).joinpath(DIRECTIVES_FILE)
    if not filepath.exists():
        return {}
    return yaml.safe_load(filepath.read_text()) or {}


def read_file(node, filename, kind):
    """Load a file as text."""
    filepath = Path(Path(node.filepath).parent, filename)
    require(filepath.exists(), f"Missing {kind} file {filename} from {node}")
    return filepath.read_text()


def read_info(filename):
    """Read YAML file from project info directory."""
    filepath = Path(ark.site.home(), "info", filename)
    return yaml.safe_load(filepath.read_text()) or {}


def require(cond, msg):
    """Fail if condition untrue."""
    if not cond:
        fail(msg)


def require_file(node, filename, kind):
    """Require that a file exists."""
    filepath = Path(Path(node.filepath).parent, filename)
    require(filepath.exists(), f"Missing {kind} file {filename} from {node}")
