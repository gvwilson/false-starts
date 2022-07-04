"""Test file writing."""

import logging
from textwrap import dedent

import pytest
import yaml

from mccole.accounting import Config, CrossRef
from mccole.collect import collect_pages
from mccole.config import DEFAULT_CONFIG_FILE, DEFAULTS, load_config
from mccole.tokenize import tokenize
from mccole.write import copy_files, generate_pages, generate_onepage


CONFIG = """\
copyrightyear: 2022
author: "Greg Wilson"
repo: https://github.com/gvwilson/mccole
tool: McCole
title: Testing
chapters:
- slug: first
  title: First
copy:
- "*/*.txt"
"""


CONFIG_2 = """\
copyrightyear: 2022
author: "Greg Wilson"
repo: https://github.com/gvwilson/mccole
tool: McCole
title: Testing
chapters:
- slug: first
  title: First
- slug: second
  title: Second
copy:
- "*/*.txt"
"""


@pytest.fixture
def config():
    combined = DEFAULTS | yaml.safe_load(CONFIG)
    return Config(**combined)


def test_copy_existing_file(fs, config):
    fs.create_file("first/a.txt", contents="AAA")
    fs.create_file("first/a.abc", contents="ABC")
    copy_files(config)
    assert fs.exists("docs/first/a.txt")
    assert not fs.exists("docs/first/a.abc")


def test_generate_single_page_with_existing_template(fs, options):
    content = "---\ntemplate: page.html\n---\nparagraph"
    fs.create_file(DEFAULT_CONFIG_FILE, contents=CONFIG)
    fs.create_file("first/index.md", contents=content)
    fs.create_file("_template/page.html", contents="success")
    config = load_config(options)
    collect_pages(config)
    tokenize(config)
    generate_pages(config, CrossRef())
    assert fs.get_object("docs/first/index.html").contents == "success"


def test_generate_single_page_with_missing_template(fs, caplog, options):
    content = "---\ntemplate: page.html\n---\nparagraph"
    fs.create_file(DEFAULT_CONFIG_FILE, contents=CONFIG)
    fs.create_file("first/index.md", contents=content)
    config = load_config(options)
    collect_pages(config)
    tokenize(config)
    with caplog.at_level(logging.WARNING):
        generate_pages(config, CrossRef())
    assert fs.get_object("docs/first/index.html").contents.strip() == "<p>paragraph</p>"
    assert len(caplog.record_tuples) == 1
    message = "Unknown template page.html in ./first/index.md."
    assert caplog.record_tuples[0][2] == message


def test_generate_multi_page_with_toc(fs, options):
    fs.create_file(DEFAULT_CONFIG_FILE, contents=CONFIG_2)
    first = "---\ntemplate: left.html\n---\nfirst"
    fs.create_file("first/index.md", contents=first)
    second = "---\ntemplate: right.html\n---\nsecond"
    fs.create_file("second/index.md", contents=second)
    fs.create_file("_template/left.html", contents="success")
    fs.create_file("_template/right.html", contents="success")
    config = load_config(options)
    collect_pages(config)
    tokenize(config)
    generate_pages(config, CrossRef())
    assert fs.get_object("docs/first/index.html").contents == "success"
    assert fs.get_object("docs/second/index.html").contents == "success"

    expected = dedent("""\
    <section id="first">
    <h1 id="first">First</h1>
    <p>first</p>
    </section>
    <section id="second">
    <h1 id="second">Second</h1>
    <p>second</p>
    </section>
    """)
    generate_onepage(config, CrossRef(), "all.html")
    assert fs.get_object("docs/all.html").contents == expected
