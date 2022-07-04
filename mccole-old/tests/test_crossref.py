"""Testing cross-references."""

import logging
from textwrap import dedent

import pytest
import yaml

from mccole.accounting import Config
from mccole.collect import collect_pages
from mccole.config import DEFAULT_CONFIG_FILE, DEFAULTS
from mccole.crossref import cross_reference
from mccole.tokenize import tokenize


def _run_test(fs, caplog, chapters):
    combined = DEFAULTS | {"chapters": chapters}
    fs.create_file(DEFAULT_CONFIG_FILE, contents=yaml.safe_dump(combined))
    config = Config(**combined)
    collect_pages(config)
    tokenize(config)
    with caplog.at_level(logging.WARNING):
        xref = cross_reference(config)
    messages = [warning[2] for warning in caplog.record_tuples]
    return xref, messages


@pytest.fixture
def empty_doc(fs):
    fs.create_file("empty/index.md", contents="")


def test_crossref_with_no_ref(fs, caplog, empty_doc):
    xref, messages = _run_test(fs, caplog, [{"slug": "empty", "title": "Empty"}])
    assert len(xref.hd_id_to_index) == 1
    assert len(xref.hd_id_to_title) == 1
    assert len(xref.hd_id_to_slug) == 1
    assert len(xref.hd_index_to_id) == 1
    assert len(messages) == 0


@pytest.fixture
def self_ref_doc(fs):
    fs.create_file(
        "self_ref/index.md",
        contents=dedent(
            """\
    <a section="self"/>
    """
        ),
    )


def test_crossref_with_self_title_ref(fs, caplog, self_ref_doc):
    xref, messages = _run_test(
        fs, caplog, [{"slug": "self_ref", "title": "Self Reference"}]
    )
    assert xref.hd_id_to_index == {"self_ref": ("1",)}
    assert xref.hd_id_to_slug == {"self_ref": "self_ref"}
    assert xref.hd_id_to_title == {"self_ref": "Self Reference"}
    assert xref.hd_index_to_id == {("1",): "self_ref"}
    assert xref.fig_id_to_index == {}
    assert xref.fig_id_to_slug == {}
    assert xref.tbl_id_to_index == {}
    assert xref.tbl_id_to_slug == {}
    assert not messages


@pytest.fixture
def other_ref_doc(fs):
    fs.create_file(
        "other_ref/index.md",
        contents=dedent(
            """\
    <a section="self"/>
    """
        ),
    )


def test_crossref_with_other_title_ref(fs, caplog, self_ref_doc, other_ref_doc):
    xref, messages = _run_test(
        fs,
        caplog,
        [
            {"slug": "self_ref", "title": "Self"},
            {"slug": "other_ref", "title": "Other"},
        ],
    )
    assert xref.hd_id_to_index == {"self_ref": ("1",), "other_ref": ("2",)}
    assert xref.hd_id_to_slug == {"self_ref": "self_ref", "other_ref": "other_ref"}
    assert xref.hd_id_to_title == {"self_ref": "Self", "other_ref": "Other"}
    assert xref.hd_index_to_id == {("1",): "self_ref", ("2",): "other_ref"}
    assert xref.fig_id_to_index == {}
    assert xref.fig_id_to_slug == {}
    assert xref.tbl_id_to_index == {}
    assert xref.tbl_id_to_slug == {}
    assert not messages


@pytest.fixture
def dup_ref_doc(fs):
    fs.create_file(
        "dup_ref/index.md",
        contents=dedent(
            """\
    ## Section 1 {#sec}

    <figure id="fig">
      <img src="fig_1.svg" alt="fig 1" />
      <figcaption>Figure Text 1</figcaption>
    </figure>

    <div class="table" id="tbl" cap="Table Text 1.">
    | Left | Right |
    | ---- | ----- |
    | 1234 | seven |
    </div>

    ## Section 2 {#sec}

    <figure id="fig">
      <img src="fig_2.svg" alt="fig 2" />
      <figcaption>Figure Text 2</figcaption>
    </figure>

    <div class="table" id="tbl" cap="Table Text 2.">
    | Left | Right |
    | ---- | ----- |
    | 1234 | seven |
    </div>
    """
        ),
    )


def test_crossref_with_duplicate_labels(fs, caplog, dup_ref_doc):
    xref, messages = _run_test(fs, caplog, [{"slug": "dup_ref", "title": "Dup"}])
    assert len(messages) == 3
    assert any("Duplicate heading label 'sec'" in m for m in messages)
    assert any("Duplicate figure label 'fig'" in m for m in messages)
    assert any("Duplicate table label 'tbl'" in m for m in messages)


@pytest.fixture
def bad_figures_doc(fs):
    fs.create_file(
        "bad_figures/index.md",
        contents=dedent(
            """\
    <figure id="fig">
      <img alt="No image file" />
      <figcaption>Figure Text 1</figcaption>
    </figure>

    <figure id="fig">
      <img src="fig_1.svg" />
      <figcaption>No alt text</figcaption>
    </figure>

    <figure id="fig">
      <img src="fig_1.svg" alt="No caption" />
    </figure>
    """
        ),
    )


def test_crossref_with_bad_figures(fs, caplog, bad_figures_doc):
    xref, messages = _run_test(
        fs, caplog, [{"slug": "bad_figures", "title": "Bad Figures"}]
    )
    assert len(messages) == 3
    assert all("Badly-formatted figure" in m for m in messages)


@pytest.fixture
def bad_tables_doc(fs):
    fs.create_file(
        "bad_tables/index.md",
        contents=dedent(
            """\
    <div class="table" cap="Missing ID">
    | Left | Right |
    | ---- | ----- |
    | 1234 | seven |
    </div>

    <div class="table" id="missing_caption">
    | Left | Right |
    | ---- | ----- |
    | 1234 | seven |
    </div>

    <div class="table" id="tbl" cap="Missing Body">
    </div>
    """
        ),
    )


def test_crossref_with_bad_tables(fs, caplog, bad_tables_doc):
    xref, messages = _run_test(
        fs, caplog, [{"slug": "bad_tables", "title": "Bad Tables"}]
    )
    assert len(messages) == 3
    assert all("Badly-formatted table" in m for m in messages)


@pytest.fixture
def unlabeled_sections_doc(fs):
    fs.create_file(
        "unlabeled_sections/index.md",
        contents=dedent(
            """\
    ## Labeled 1 {#labeled_1}
    ## Unlabeled 2
    ### Unlabeled Third Level
    ## Labeled 3 {#labeled_3}
    ### Labeled Third Level {#labeled_3_subsection}
    ## Unlabeled Fourth Level
    """
        ),
    )


def test_crossref_with_unlabeled_sections(fs, caplog, unlabeled_sections_doc):
    xref, messages = _run_test(
        fs, caplog, [{"slug": "unlabeled_sections", "title": "Unlabeled Sections"}]
    )
    assert xref.hd_id_to_index == {
        "unlabeled_sections": ("1",),
        "labeled_1": ("1", "1"),
        "labeled_3": ("1", "3"),
        "labeled_3_subsection": ("1", "3", "1"),
    }
    assert xref.hd_id_to_title == {
        "unlabeled_sections": "Unlabeled Sections",
        "labeled_1": "Labeled 1",
        "labeled_3": "Labeled 3",
        "labeled_3_subsection": "Labeled Third Level",
    }
    assert all(slug == "unlabeled_sections" for slug in xref.hd_id_to_slug.values())
    assert xref.hd_index_to_id == {
        ("1",): "unlabeled_sections",
        ("1", "1"): "labeled_1",
        ("1", "3"): "labeled_3",
        ("1", "3", "1"): "labeled_3_subsection",
    }
    assert len(messages) == 0


@pytest.fixture
def sudden_change_sections_doc(fs):
    fs.create_file(
        "sudden_change_sections/index.md",
        contents=dedent(
            """\
    ### Third Level {#third}
    """
        ),
    )


def test_crossref_with_sudden_change_sections(fs, caplog, sudden_change_sections_doc):
    xref, messages = _run_test(
        fs, caplog, [{"slug": "sudden_change_sections", "title": "Sudden Change"}]
    )
    assert xref.hd_id_to_index == {
        "sudden_change_sections": ("1",),
        "third": ("1", "1", "1"),
    }
    assert xref.hd_id_to_title == {
        "sudden_change_sections": "Sudden Change",
        "third": "Third Level",
    }
    assert all(slug == "sudden_change_sections" for slug in xref.hd_id_to_slug.values())
    assert xref.hd_index_to_id == {
        ("1",): "sudden_change_sections",
        ("1", "1", "1"): "third",
    }
    assert len(messages) == 1


@pytest.fixture
def drop_multiple_levels(fs):
    fs.create_file(
        "drop_multiple_levels/index.md",
        contents=dedent(
            """\
    ## Unlabeled Second
    ### Unlabeled Third
    #### Unlabeled Fourth
    ## Second Level {#second}
    """
        ),
    )


def test_crossref_drop_multiple_levels(fs, caplog, drop_multiple_levels):
    xref, messages = _run_test(
        fs, caplog, [{"slug": "drop_multiple_levels", "title": "Drop Multiple"}]
    )
    assert xref.hd_id_to_index == {
        "drop_multiple_levels": ("1",),
        "second": ("1", "2"),
    }
    assert xref.hd_id_to_title == {
        "drop_multiple_levels": "Drop Multiple",
        "second": "Second Level",
    }
    assert xref.hd_index_to_id == {
        ("1",): "drop_multiple_levels",
        ("1", "2"): "second",
    }
    assert len(messages) == 0


@pytest.fixture
def with_blockquote(fs):
    fs.create_file(
        "blockquote/index.md",
        contents=dedent(
            """\
            ## Before {#before}
            > ### Block
            > body
            ## After {#after}
            ### Triple
            """
        ),
    )


def test_crossref_with_blockquote(fs, caplog, with_blockquote):
    xref, messages = _run_test(
        fs, caplog, [{"slug": "blockquote", "title": "Blockquote"}]
    )
    assert xref.hd_id_to_index == {'blockquote': ('1',), 'before': ('1', '1'), 'after': ('1', '2')}
    assert xref.hd_id_to_slug == {'blockquote': 'blockquote', 'before': 'blockquote', 'after': 'blockquote'}
    assert xref.hd_id_to_title == {'blockquote': 'Blockquote', 'before': 'Before', 'after': 'After'}
    assert xref.hd_index_to_id == {('1',): 'blockquote', ('1', '1'): 'before', ('1', '2'): 'after'}
    assert len(messages) == 0


@pytest.fixture
def with_h1(fs):
    fs.create_file(
        "h1/index.md",
        contents=dedent(
            """\
            # Title
            ## Heading {#heading}
            """
        ),
    )


def test_crossref_with_h1(fs, caplog, with_h1):
    xref, messages = _run_test(
        fs, caplog, [{"slug": "h1", "title": "Title"}]
    )
    assert xref.hd_id_to_index == {'h1': ('1',), 'heading': ('1', '1')}
    assert xref.hd_id_to_slug == {'h1': 'h1', 'heading': 'h1'}
    assert xref.hd_id_to_title == {'h1': 'Title', 'heading': 'Heading'}
    assert xref.hd_index_to_id == {('1',): 'h1', ('1', '1'): 'heading'}
    assert len(messages) == 0
