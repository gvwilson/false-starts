"""Test template fill-in."""

import logging
from textwrap import dedent

from mccole.accounting import Config, CrossRef, Info, Seen
from mccole.crossref import CrossRef
from mccole.gloss import GlossaryEntry
from mccole.template import fill_template, load_templates, make_site_object


def _setup():
    config = Config()
    seen = Seen()
    xref = CrossRef()
    info = Info()
    site = make_site_object(config, seen)
    return config, seen, xref, info, site


def test_template_loading(fs):
    fs.create_file("_template/first.html", contents="content")
    fs.create_file("_template/second.html", contents="content")
    config = Config()
    load_templates(config)
    assert len(config.template) == 2


def test_template_cannot_load_with_triple_quote(fs, caplog):
    fs.create_file("_template/first.html", contents="'''test this'''")
    config = Config()
    with caplog.at_level(logging.WARNING):
        load_templates(config)
    assert len(config.template) == 1
    assert len(caplog.record_tuples) == 1


def test_template_fill_empty():
    config, seen, xref, info, site = _setup()
    html = fill_template(config, xref, info, site, "")
    assert html == ""


def test_template_cannot_contain_triple_quote(caplog):
    config, seen, xref, info, site = _setup()
    config.author = "Some Person"
    config.template = {"test.html": "'''not allowed'''"}
    info.template = "test.html"
    html = fill_template(config, xref, info, site, "")
    assert html == ""
    assert len(caplog.record_tuples) == 1


def test_template_unknown_site_key(caplog):
    config, seen, xref, info, site = _setup()
    config.author = "Some Person"
    config.template = {"test.html": "{site.unknown()}"}
    info.template = "test.html"
    html = fill_template(config, xref, info, site, "")
    assert not html.strip()
    assert len(caplog.record_tuples) == 1


def test_template_site_author():
    config, seen, xref, info, site = _setup()
    config.author = "Some Person"
    config.template = {"test.html": "{site.author()}"}
    info.template = "test.html"
    html = fill_template(config, xref, info, site, "")
    assert html == "Some Person"


def test_template_site_copyrightyear():
    config, seen, xref, info, site = _setup()
    config.copyrightyear = "1234"
    config.template = {"test.html": "{site.copyrightyear()}"}
    info.template = "test.html"
    html = fill_template(config, xref, info, site, "")
    assert html == "1234"


def test_template_site_links():
    config, seen, xref, info, site = _setup()
    config.title = "Test"
    config.template = {"test.html": "{site.links()}"}
    config.links_data = [
        {"key": "alpha", "url": "http://alpha.site", "title": "Alpha"},
        {"key": "beta", "url": "http://beta.site", "title": "Beta"}
    ]
    info.template = "test.html"
    html = fill_template(config, xref, info, site, "")
    expected = dedent(
        """\
        <table class="links">
        <tr><th>Title</th><th>URL</th></tr>
        <tr><td>Alpha</td><td><a href="http://alpha.site">http://alpha.site</a></td></tr>
        <tr><td>Beta</td><td><a href="http://beta.site">http://beta.site</a></td></tr>
        </table>
        """
    )


def test_template_site_title():
    config, seen, xref, info, site = _setup()
    config.title = "Test"
    config.template = {"test.html": "{site.title()}"}
    info.template = "test.html"
    html = fill_template(config, xref, info, site, "")
    assert html == "Test"


def test_template_site_toc_empty():
    config, seen, xref, info, site = _setup()
    config.root = "index.md"
    info.template = "index.html"
    config.template = {"index.html": "{site.toc(1)}"}
    html = fill_template(config, xref, info, site, "")
    assert html == ""


def test_template_site_toc():
    config, seen, xref, info, site = _setup()

    config.pages = [
        Info(major="1", slug="first", lede="first lede"),
        Info(major="2", slug="second", lede="second lede")
    ]
    config.template = {"test.html": "{site.toc(1)}"}

    xref.hd_id_to_title = {"first": "First", "second": "Second"}

    info.template = "test.html"

    html = fill_template(config, xref, info, site, "")
    expected = dedent(
        """\
        <table class="toc">
        <tr><td class="toc-index">1</td><td><a href="./first/">First</a></td><td>first lede</td></tr>
        <tr><td class="toc-index">2</td><td><a href="./second/">Second</a></td><td>second lede</td></tr>
        </table>
        """
    )
    assert html == expected


def test_template_site_foot():
    config = Config()
    config.template = {
        "foot.html": "FOOTER",
        "test.html": '{site.foot("..")}'
    }

    seen = Seen()
    xref = CrossRef()

    info = Info()
    info.template = "test.html"

    site = make_site_object(config, seen)

    html = fill_template(config, xref, info, site, "")
    assert html == "FOOTER"


def test_template_site_head():
    config = Config()
    config.template = {
        "head.html": "HEADER",
        "test.html": '{site.head("..")}'
    }

    seen = Seen()
    xref = CrossRef()

    info = Info()
    info.template = "test.html"

    site = make_site_object(config, seen)

    html = fill_template(config, xref, info, site, "")
    assert html == "HEADER"


def test_template_site_stats():
    config = Config()
    config.template = {
        "stats.html": "STATS",
        "test.html": '{site.stats()}'
    }

    seen = Seen()
    xref = CrossRef()

    info = Info()
    info.template = "test.html"

    site = make_site_object(config, seen)

    html = fill_template(config, xref, info, site, "")
    assert html == "STATS"


def test_template_page_keyterms():
    config, seen, xref, info, site = _setup()

    config.lang = "fr"
    config.template = {"test.html": "{page.keyterms()}"}
    config.gloss_data = [
        GlossaryEntry({"key": "alpha", "fr": {"term": "Alpha", "def": "definition"}})
    ]

    info.keyterms = {"alpha"}
    info.template = "test.html"
    info.to_root = ".."

    html = fill_template(config, xref, info, site, "")
    assert html == '<div class="keyterms"><p><a href="../glossary/#alpha">Alpha</a></p></div>\n'


def test_template_page_keyterms_empty():
    config, seen, xref, info, site = _setup()

    config.lang = "fr"
    config.template = {"test.html": "{page.keyterms()}"}
    config.gloss_data = [
        GlossaryEntry({"key": "alpha", "fr": {"term": "Alpha", "def": "definition"}})
    ]

    info.keyterms = set()
    info.template = "test.html"
    info.to_root = ".."

    html = fill_template(config, xref, info, site, "")
    assert html == ""


def test_template_page_lede():
    config, seen, xref, info, site = _setup()
    config.template = {"test.html": "{page.lede()}"}
    info.slug = "topic"
    info.lede = "the lede"
    info.template = "test.html"
    html = fill_template(config, xref, info, site, "")
    assert html == '<div class="lede"><p>the lede</p></div>'


def test_template_page_lede_empty():
    config, seen, xref, info, site = _setup()
    config.template = {"test.html": "{page.lede()}"}
    info.slug = "topic"
    info.template = "test.html"
    html = fill_template(config, xref, info, site, "")
    assert html == ""


def test_template_page_toc_empty():
    config, seen, xref, info, site = _setup()

    config.template = {"test.html": "{page.toc()}"}

    info.major = "A"
    info.slug = "topic"
    info.template = "test.html"

    xref.hd_index_to_id = {
        ("A",): "a",
        ("B",): "b",
    }
    xref.hd_id_to_title = {
        "a": "A Title",
        "b": "B Title",
    }

    html = fill_template(config, xref, info, site, "")
    assert html == ""


def test_template_page_toc():
    config, seen, xref, info, site = _setup()

    config.template = {"test.html": "{page.toc()}"}

    info.major = "A"
    info.slug = "topic"
    info.template = "test.html"

    xref.hd_index_to_id = {
        ("A",): "a",
        ("A", 1): "a-sub",
        ("A", 2): "a-sub-2",
        ("B",): "b",
        ("B", 1): "b-sub"
    }
    xref.hd_id_to_title = {
        "a": "A Title",
        "a-sub": "A Subtitle",
        "a-sub-2": "Another Subtitle",
        "b": "B Title",
        "b-sub": "B Subtitle"
    }

    html = fill_template(config, xref, info, site, "")
    expected = dedent(
        """\
        <ol class="toc">
        <li><a href="#a-sub">A Subtitle</a></li>
        <li><a href="#a-sub-2">Another Subtitle</a></li>
        </ol>
        """
    )
    assert html == expected


def test_template_all_in_one_toc():
    config, seen, xref, info, site = _setup()

    config.pages = [
        Info(slug="a", major="A"),
        Info(slug="b", major="B"),
        Info(slug="c", major="C")
    ]

    config.template = {"test.html": "{site.toc(2)}"}

    info.major = "A"
    info.slug = "topic"
    info.template = "test.html"

    xref.hd_index_to_id = {
        ("A",): "a",
        ("A", 1): "a-sub",
        ("A", 2): "a-sub-2",
        ("B",): "b",
        ("B", 1): "b-sub"
    }
    xref.hd_id_to_title = {
        "a": "A Title",
        "a-sub": "A Subtitle",
        "a-sub-2": "Another Subtitle",
        "b": "B Title",
        "b-sub": "B Subtitle"
    }

    html = fill_template(config, xref, info, site, "")
    expected = [
        '<ol class="toc">',
        '<li value="A"><a href="#a">A Title</a>',
        '<li><a href="#a-sub">A Subtitle</a></li>',
        '<li><a href="#a-sub-2">Another Subtitle</a></li>',
        '</ol>',
        '</li>',
        '<li value="B"><a href="#b">B Title</a>',
        '<li><a href="#b-sub">B Subtitle</a></li>',
    ]
    assert all(e in html for e in expected)
