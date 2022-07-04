"""Test page collection."""

from textwrap import dedent

import pytest
import yaml

from mccole.accounting import Config, Info
from mccole.collect import collect_pages
from mccole.util import McColeExc


def test_collect_chapters_key_missing():
    assert collect_pages(Config()) == []


def test_collect_single_chapter():
    config = Config(src="src", dst="dst", chapters=[{"slug": "first", "title": "First"}])
    collect_pages(config)
    assert config.pages == [
        Info(
            slug="first",
            title="First",
            to_root="..",
            src="src/first/index.md",
            dst="dst/first/index.html",
            major=1,
            template=None,
            tokens=None,
        )
    ]


def test_collect_chapters_and_appendices():
    config = Config(src="src", dst="dst", chapters=[
        {"slug": "first", "title": "First"},
        {"slug": "second", "title": "Second"},
        {"slug": "third", "title": "Third", "appendix": True},
        {"slug": "fourth", "title": "Fourth"},
    ])
    collect_pages(config)
    assert [e.slug for e in config.pages] == [
        "first",
        "second",
        "third",
        "fourth",
    ]
    assert [e.major for e in config.pages] == [1, 2, "A", "B"]


def test_collect_with_root():
    config = Config(src="src", dst="dst", root="test.md", chapters=[
        {"slug": "first", "title": "First"}
    ])
    collect_pages(config)
    assert len(config.pages) == 2
    index_entry = Info(
        slug="_index",
        to_root=".",
        src="src/test.md",
        dst="dst/index.html",
        major=None,
        template="index.html",
        tokens=None,
    )
    assert index_entry in config.pages
    chapter_entry = Info(
        slug="first",
        title="First",
        to_root="..",
        src="src/first/index.md",
        dst="dst/first/index.html",
        major=1,
        template=None,
        tokens=None,
    )
    assert chapter_entry in config.pages


def test_collect_missing_slug():
    config = Config(src="src", dst="dst", chapters=[
        {"slug": "first", "title": "First"},
        {"key": "value"}
    ])
    with pytest.raises(McColeExc):
        collect_pages(config)


def test_collect_explicit_source_file():
    config = Config(src="src", dst="dst", chapters=[
        {"slug": "first", "title": "First", "file": "something.md"}
    ])
    collect_pages(config)
    assert config.pages == [
        Info(
            slug="first",
            title="First",
            to_root="..",
            src="src/something.md",
            dst="dst/first/index.html",
            major=1,
            template=None,
            tokens=None,
        )
    ]
