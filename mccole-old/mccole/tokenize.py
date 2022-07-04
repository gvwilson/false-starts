"""Turn chapters into tokens."""

import yaml

import frontmatter

from .patterns import GLOSS_REF, GLOSS_INDEX
from .util import make_md


def make_markdown_links(config):
    """Make Markdown links table from configuration."""
    if not config.links_data:
        return ""
    return "\n\n" + "\n".join(
        f"[{ln['key']}]: {ln['url']}" for ln in config.links_data
    )


def tokenize(config):
    """Parse each file in turn."""
    md = make_md()
    links_table = make_markdown_links(config)
    for info in config.pages:
        with open(info.src, "r") as reader:
            info.metadata, info.text = frontmatter.parse(reader.read())
            info.tokens = md.parse(info.text + links_table)
            info.keyterms = _get_keyterms(info.tokens)


# ----------------------------------------------------------------------


def _get_keyterms(tokens):
    """Collect all glossary items in the file."""
    keyterms = set()
    for token in tokens:
        if token.type != "inline":
            continue
        for child in token.children:
            if child.type != "html_inline":
                continue
            for key in GLOSS_REF.findall(token.content):
                keyterms.add(key)
            for match in GLOSS_INDEX.findall(token.content):
                keyterms.add(match[0])
    return keyterms
