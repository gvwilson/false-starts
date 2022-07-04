"""Test rendering."""

import logging
from textwrap import dedent

import pytest

from mccole.accounting import Config, CrossRef, Info, Seen
from mccole.render import render
from mccole.util import make_md

FILENAME = "source/index.md"


@pytest.fixture
def config():
    return Config(bib_keys={}, lang="en", pages={"major": 1})


@pytest.fixture
def empty_seen():
    return Seen()


@pytest.fixture
def empty_xref():
    return CrossRef()


def _Info(text, **kwargs):
    result = Info(src=FILENAME, tokens=make_md().parse(text), to_root=".")
    for (k, v) in kwargs.items():
        setattr(result, k, v)
    return result


def test_render_empty_document(config, empty_xref, empty_seen):
    assert render(config, empty_xref, empty_seen, _Info("")) == ""


def test_render_simple_html(config, empty_xref, empty_seen):
    text = "try <em>italics</em> and <code>code</code><br/>line break"
    expected = f"<p>{text}</p>\n"
    assert render(config, empty_xref, empty_seen, _Info(text)) == expected


def test_render_single_paragraph(config, empty_xref, empty_seen):
    html = render(config, empty_xref, empty_seen, _Info("paragraph"))
    assert html == "<p>paragraph</p>\n"


def test_render_headings(config, empty_xref, empty_seen):
    text = dedent(
        """\
    # Title {#title}
    ## Section {#section}
    ## Unlabelled
    ### Exercise {.exercise}
    """
    )
    html = render(config, empty_xref, empty_seen, _Info(text))
    expected = dedent(
        """\
    <h1 id="title">Title</h1>
    <h2 id="section">Section</h2>
    <h2>Unlabelled</h2>
    <h3 class="exercise">Exercise</h3>
    """
    )
    assert html == expected


def test_render_citation(config, empty_xref, empty_seen):
    text = "<cite>Key1,Key2</cite>"
    html = render(config, empty_xref, empty_seen, _Info(text))
    assert (
        '[<a href="../bibliography/#Key1">Key1</a>, '
        '<a href="../bibliography/#Key2">Key2</a>]'
    ) in html


def test_render_comment(config, empty_xref, empty_seen):
    text = dedent(
        """\
    before
    <!-- comment -->"
    after
    """
    )
    html = render(config, empty_xref, empty_seen, _Info(text))
    expected = dedent(
        """\
    <p>before</p>
    <!-- comment -->"
    <p>after</p>
    """
    )
    assert html == expected


def test_render_crossref_section_missing(config, empty_xref, empty_seen):
    text = dedent(
        """\
    # Title {#title}
    ## Section {#section}
    <a section="title"/> and <a section="section"/>
    """
    )
    html = render(config, empty_xref, empty_seen, _Info(text, src=FILENAME))
    assert (
        '<p><a class="secref" href="MISSING">MISSING</a> '
        'and <a class="secref" href="MISSING">MISSING</a></p>'
    ) in html


def test_render_crossref_section_present(config, empty_xref, empty_seen):
    text = dedent(
        """\
    # Title {#title}
    ## Section {#section}
    <a section="title"/> and <a section="section"/>
    """
    )
    xref = CrossRef(
        hd_id_to_index={"title": ("1",), "section": ("1", "1")},
        hd_id_to_slug={"title": "source", "section": "source"},
        hd_id_to_title={"title": "Title", "section": "Section"},
        hd_index_to_id={("1",): "title", ("1", "1"): "section"},
    )
    html = render(
        config, xref, empty_seen, _Info(text, slug="source", src=FILENAME)
    )
    assert (
        '<p><a class="secref" href="#title">Chapter&nbsp;1</a> '
        'and <a class="secref" href="#section">Section&nbsp;1.1</a></p>'
    ) in html


def test_render_crossref_appendix(config, empty_xref, empty_seen):
    text = dedent(
        """\
    # Title {#title}
    ## Section {#section}
    <a section="title"/> and <a section="section"/>
    """
    )
    xref = CrossRef(
        hd_id_to_index={"title": ("A",), "section": ("A", "1")},
        hd_id_to_slug={"title": "source", "section": "source"},
        hd_id_to_title={"title": "Title", "section": "Section"},
        hd_index_to_id={("A",): "title", ("A", "1"): "section"},
    )
    html = render(
        config, xref, empty_seen, _Info(text, slug="source", src=FILENAME)
    )
    assert (
        '<p><a class="secref" href="#title">Appendix&nbsp;A</a> '
        'and <a class="secref" href="#section">Section&nbsp;A.1</a></p>'
    ) in html


def test_render_figure_with_id(config, empty_xref, empty_seen):
    xref = CrossRef(
        fig_id_to_index={"short-figure": ("1", "1")},
        fig_id_to_slug={"short-figure": "source"},
    )
    text = dedent(
        """\
    <figure id="short-figure">
      <img src="figures/short.svg" alt="Short caption" />
      <figcaption>Long version of short caption.</figcaption>
    </figure>
    """
    )
    html = render(config, xref, empty_seen, _Info(text))
    expected = dedent(
        """\
    <figure id="short-figure">
      <img src="figures/short.svg" alt="Short caption" />
      <figcaption>Figure&nbsp;1.1: Long version of short caption.</figcaption>
    </figure>
    """
    )
    assert html == expected


def test_render_figure_without_id(config, empty_xref, empty_seen):
    xref = CrossRef()
    text = dedent(
        """\
    <figure>
      <img src="figures/short.svg" alt="Short caption" />
      <figcaption>Long version of short caption.</figcaption>
    </figure>
    """
    )
    html = render(config, xref, empty_seen, _Info(text))
    expected = dedent(
        """\
    <figure>
      <img src="figures/short.svg" alt="Short caption" />
      <figcaption>Long version of short caption.</figcaption>
    </figure>
    """
    )
    assert html == expected


def test_render_figure_with_unknown_id(caplog, config, empty_xref, empty_seen):
    xref = CrossRef()
    text = dedent(
        """\
    <figure id="short-figure">
      <img src="figures/short.svg" alt="Short caption" />
      <figcaption>Long version of short caption.</figcaption>
    </figure>
    """
    )
    with caplog.at_level(logging.WARNING):
        html = render(config, xref, empty_seen, _Info(text))
    expected = dedent(
        """\
    <figure id="short-figure">
      <img src="figures/short.svg" alt="Short caption" />
      <figcaption>Figure&nbsp;MISSING: Long version of short caption.</figcaption>
    </figure>
    """
    )
    assert html == expected
    assert len(caplog.record_tuples) == 1


def test_render_figure_ref_with_known_key(config, empty_xref, empty_seen):
    xref = CrossRef(
        fig_id_to_index={"key": ("A", "2")}, fig_id_to_slug={"key": "elsewhere"}
    )
    text = '<a figure="key"/>'
    html = render(
        config, xref, empty_seen, _Info(text, slug="source", to_root="..")
    )
    assert '<a class="figref" href="../elsewhere/#key">Figure&nbsp;A.2</a>' in html


def test_render_figure_ref_with_unknown_key(caplog, config, empty_xref, empty_seen):
    text = '<a figure="key"/>'
    info = _Info(text)
    with caplog.at_level(logging.WARNING):
        html = render(config, empty_xref, empty_seen, info)
    assert '<a class="figref" href="MISSING">Figure&nbsp;MISSING</a>' in html
    assert len(caplog.record_tuples) == 1


def test_render_gloss_def(config, empty_xref, empty_seen):
    config.gloss_keys = {"key"}
    text = '<span g="key">text</span>'
    html = render(config, empty_xref, empty_seen, _Info(text))
    assert '<span g="key">text</span>' in html


def test_render_gloss_index_def(config, empty_xref, empty_seen):
    config.gloss_keys = {"key"}
    text = '<span g="key" i="term">text</span>'
    html = render(config, empty_xref, empty_seen, _Info(text))
    assert '<span g="key" i="term">text</span>' in html


def test_render_inclusion(fs, caplog, config, empty_xref, empty_seen):
    fs.create_file("source/test.py", contents="content")
    text = '<div class="include" file="test.py" />'
    with caplog.at_level(logging.WARNING):
        html = render(config, empty_xref, empty_seen, _Info(text))
    expected = dedent(
        """\
    <pre title="test.py"><code class="language-py">content
    </code></pre>
    """
    )
    assert html == expected


def test_render_index_def(config, empty_xref, empty_seen):
    text = '<span i="first; second!third">text</span>'
    html = render(config, empty_xref, empty_seen, _Info(text))
    assert '<span i="first; second!third">text</span>' in html


def test_render_raw_table(config, empty_xref, empty_seen):
    text = dedent("""\
    <table>
    <tr><td>(4x + 8)/2</td><td>=</td><td>5</td></tr>
    <tr><td>4x + 8</td><td>=</td><td>2 * 5</td></tr>
    </table>
    """)
    html = render(config, empty_xref, empty_seen, _Info(text))
    assert html.strip() == text.strip()


def test_render_table_correct(config, empty_xref, empty_seen):
    xref = CrossRef(tbl_id_to_index={"short-table": (1, 1)})
    text = dedent(
        """\
    <div class="table" id="short-table" cap="Short table caption.">
    | Left | Right |
    | ---- | ----- |
    | 1    | alpha |
    </div>
    """
    )
    html = render(config, xref, empty_seen, _Info(text))
    expected = dedent(
        """\
    <table id="short-table"><caption>Table&nbsp;1.1: Short table caption.</caption>
    <thead>
    <tr>
    <th>Left</th>
    <th>Right</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>1</td>
    <td>alpha</td>
    </tr>
    </tbody>
    </table>
    """
    )
    assert html == expected


def test_render_table_missing_id(caplog, config, empty_xref, empty_seen):
    xref = CrossRef(tbl_id_to_index={"short-table": (1, 1)})
    text = dedent(
        """\
    <div class="table" cap="Short table caption.">
    | Left | Right |
    | ---- | ----- |
    | 1    | alpha |
    </div>
    """
    )
    with caplog.at_level(logging.WARNING):
        html = render(config, xref, empty_seen, _Info(text))
    expected = dedent(
        """\
        <table id="MISSING"><caption>Table&nbsp;MISSING: Short table caption.</caption>
        <thead>
        <tr>
        <th>Left</th>
        <th>Right</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>1</td>
        <td>alpha</td>
        </tr>
        </tbody>
        </table>
        """
    )
    assert len(caplog.record_tuples) == 1


def test_render_table_bad_caption(caplog, config, empty_xref, empty_seen):
    xref = CrossRef(tbl_id_to_index={"short-table": (1, 1)})
    text = dedent(
        """\
    <div class="table" id="short-table" caption="Caption instead of cap.">
    | Left | Right |
    | ---- | ----- |
    | 1    | alpha |
    </div>
    """
    )
    with caplog.at_level(logging.WARNING):
        html = render(config, xref, empty_seen, _Info(text))
    expected = dedent(
        """\
        <table id="short-table"><caption>Table&nbsp;1.1: MISSING.</caption>
        <thead>
        <tr>
        <th>Left</th>
        <th>Right</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>1</td>
        <td>alpha</td>
        </tr>
        </tbody>
        </table>
        """
    )
    assert len(caplog.record_tuples) == 1


def test_render_table_no_title_line(caplog, config, empty_xref, empty_seen):
    xref = CrossRef(tbl_id_to_index={"short-table": (1, 1)})
    text = dedent(
        """\
    <div class="table" id="short-table" cap="Caption cap.">
    | 1    | alpha |
    </div>
    """
    )
    with caplog.at_level(logging.WARNING):
        html = render(config, xref, empty_seen, _Info(text))
    expected = "<p>| 1    | alpha |</p>"
    assert html.strip() == expected.strip()
    assert len(caplog.record_tuples) == 0


def test_render_table_no_body(caplog, config, empty_xref, empty_seen):
    xref = CrossRef(tbl_id_to_index={"short-table": (1, 1)})
    text = dedent(
        """\
    <div class="table" id="short-table" cap="Caption cap.">
    </div>
    """
    )
    with caplog.at_level(logging.WARNING):
        html = render(config, xref, empty_seen, _Info(text))
    assert html.strip() == "MISSING"
    assert len(caplog.record_tuples) == 1


def test_render_table_ref_with_known_key(config, empty_xref, empty_seen):
    xref = CrossRef(
        tbl_id_to_index={"key": ("A", 2)},
        tbl_id_to_slug={"key": "elsewhere"},
    )
    text = '<a table="key"/>'
    html = render(
        config, xref, empty_seen, _Info(text, slug="source", to_root="..")
    )
    assert '<a class="tblref" href="../elsewhere/#key">Table&nbsp;A.2</a>' in html


def test_render_table_ref_with_unknown_key(caplog, config, empty_xref, empty_seen):
    text = '<a table="key"/>'
    info = _Info(text)
    with caplog.at_level(logging.WARNING):
        html = render(config, empty_xref, empty_seen, info)
    assert '<a class="tblref" href="MISSING">Table&nbsp;MISSING</a>' in html
    assert len(caplog.record_tuples) == 1


def test_render_unknown_html(caplog, config, empty_xref, empty_seen):
    text = "<something>text</something>"
    info = _Info(text)
    with caplog.at_level(logging.WARNING):
        html = render(config, empty_xref, empty_seen, info)
    assert text in html
    assert len(caplog.record_tuples) == 2


def test_render_linecount_file_present(fs, caplog, config, empty_xref, empty_seen):
    text = '<span class="linecount" file="test.py"/>'
    code = "first\nsecond\nthird"
    fs.create_file("source/test.py", contents=code)
    info = _Info(text)
    with caplog.at_level(logging.WARNING):
        html = render(config, empty_xref, empty_seen, info)
    assert html == "3"
    assert len(caplog.record_tuples) == 0


def test_render_linecount_file_missing(fs, caplog, config, empty_xref, empty_seen):
    text = '<span class="linecount" file="test.py"/>'
    code = "first\nsecond\nthird"
    info = _Info(text)
    with caplog.at_level(logging.WARNING):
        html = render(config, empty_xref, empty_seen, info)
    assert html == "MISSING"
    assert len(caplog.record_tuples) == 1
