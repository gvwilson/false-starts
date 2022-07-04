"""Test tokenization."""

import pytest
import yaml

from mccole.accounting import Config
from mccole.collect import collect_pages
from mccole.config import DEFAULTS
from mccole.tokenize import tokenize

ONE_CHAPTER = """\
chapters:
- slug: first
  title: First
"""

LINKS = """\
- key: ident
  url: url
  title: title
"""


@pytest.fixture
def config():
    combined = DEFAULTS | yaml.safe_load(ONE_CHAPTER)
    return Config(**combined)


def _match(token, required):
    return all(getattr(token, k) == required[k] for k in required)


def test_tokenize_empty_doc(fs, config):
    fs.create_file("./first/index.md", contents="")
    collect_pages(config)
    tokenize(config)
    tokens = config.pages[0].tokens
    assert tokens == []


def test_tokenize_title(fs, config):
    fs.create_file("./first/index.md", contents="# Title")
    collect_pages(config)
    tokenize(config)
    tokens = config.pages[0].tokens

    assert len(tokens) == 3
    assert _match(tokens[0], {"type": "heading_open", "tag": "h1"})
    assert _match(tokens[1], {"type": "inline"})
    assert _match(tokens[2], {"type": "heading_close", "tag": "h1"})

    assert len(tokens[1].children) == 1
    assert _match(tokens[1].children[0], {"type": "text", "content": "Title"})


def test_tokenize_paragraph(fs, config):
    fs.create_file("./first/index.md", contents="paragraph")
    collect_pages(config)
    tokenize(config)
    tokens = config.pages[0].tokens

    assert len(tokens) == 3
    assert _match(tokens[0], {"type": "paragraph_open", "tag": "p"})
    assert _match(tokens[1], {"type": "inline"})
    assert _match(tokens[2], {"type": "paragraph_close", "tag": "p"})

    assert len(tokens[1].children) == 1
    assert _match(tokens[1].children[0], {"type": "text", "content": "paragraph"})


def test_tokenize_with_front_matter(fs, config):
    fs.create_file("./first/index.md", contents="---\nleft: right\n---\nparagraph")
    collect_pages(config)
    tokenize(config)
    assert config.pages[0].metadata == {"left": "right"}
    tokens = config.pages[0].tokens
    assert tokens[0].type == "paragraph_open"
    assert tokens[1].content.strip() == "paragraph"


def test_tokenize_with_links_table(fs, config):
    config.links_data = yaml.safe_load(LINKS)
    fs.create_file("./first/index.md", contents="[body][ident]")
    collect_pages(config)
    tokenize(config)
    tokens = config.pages[0].tokens

    assert len(tokens) == 3
    assert _match(tokens[0], {"type": "paragraph_open", "tag": "p"})
    assert _match(tokens[1], {"type": "inline"})
    assert _match(tokens[2], {"type": "paragraph_close", "tag": "p"})

    assert _match(
        tokens[1].children[0], {"type": "link_open", "attrs": {"href": "url"}}
    )
    assert _match(tokens[1].children[1], {"type": "text", "content": "body"})
    assert _match(tokens[1].children[2], {"type": "link_close"})


def test_tokenize_gloss_ref(fs, config):
    fs.create_file("./first/index.md", contents='<span g="gkey">text</span>')
    collect_pages(config)
    tokenize(config)
    assert config.pages[0].keyterms == {'gkey'}


def test_tokenize_gloss_index(fs, config):
    fs.create_file("./first/index.md", contents='<span g="gkey" i="something">text</span>')
    collect_pages(config)
    tokenize(config)
    assert config.pages[0].keyterms == {'gkey'}
