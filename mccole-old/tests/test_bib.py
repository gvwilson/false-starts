"""Test bibliography."""

import logging
from textwrap import dedent

import pytest

from mccole.accounting import Config
from mccole.bib import bib_to_html, load_bib
from mccole.util import McColeExc


def test_bib_empty_when_not_specified(fs):
    config = Config()
    load_bib(config)
    assert config.bib_data == []
    assert config.bib_keys == set()


def test_bib_fail_with_nonexistent_file(fs):
    config = Config(bib="test.bib")
    with pytest.raises(McColeExc):
        load_bib(config)


def test_bib_load_empty_file_when_present(fs):
    fs.create_file("test.bib", contents="")
    config = Config(bib="test.bib")
    load_bib(config)
    assert config.bib_data == []
    assert config.bib_keys == set()


def test_bib_load_file_containing_data(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @book{Key1234,
      author = {Some Key},
      title = {Some Title},
      publisher = {Some Publisher},
      year = {1234},
      isbn = {978-1234567890},
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    assert len(config.bib_data) == 1
    assert config.bib_data[0]["ID"] == "Key1234"
    assert config.bib_keys == {"Key1234"}


def test_bib_convert_article_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @article{Key1234,
      author = {A B and C D},
      title = {Some paper},
      journal = {Journal},
      month = {1},
      year = {1234},
      publisher = {Some Publisher},
      doi = {12.34/56-78-90}
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">A B and C D: '
        '"Some paper". <em>Journal</em>, Jan 1234, Some Publisher, '
        '<a href="https://doi.org/12.34/56-78-90">12.34/56-78-90</a>.</span>' in html
    )


def test_bib_convert_article_without_doi_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @article{Key1234,
      author = {A B and C D},
      title = {Some paper},
      journal = {Journal},
      month = {1},
      year = {1234},
      publisher = {Some Publisher}
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">A B and C D: '
        '"Some paper". <em>Journal</em>, Jan 1234, Some Publisher.</span>' in html
    )


def test_bib_convert_article_volume_number_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @article{Key1234,
      author = {A B and C D},
      title = {Some paper},
      journal = {Journal},
      month = {1},
      year = {1234},
      number = {7},
      volume = {3},
      publisher = {Some Publisher},
      doi = {12.34/56-78-90}
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">A B and C D: '
        '"Some paper". <em>Journal</em>, 3(7), Jan 1234, Some Publisher, '
        '<a href="https://doi.org/12.34/56-78-90">12.34/56-78-90</a>.</span>' in html
    )


def test_bib_convert_article_volume_without_number_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @article{Key1234,
      author = {A B and C D},
      title = {Some paper},
      journal = {Journal},
      month = {1},
      year = {1234},
      volume = {3},
      publisher = {Some Publisher},
      doi = {12.34/56-78-90}
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">A B and C D: '
        '"Some paper". <em>Journal</em>, 3, Jan 1234, Some Publisher, '
        '<a href="https://doi.org/12.34/56-78-90">12.34/56-78-90</a>.</span>' in html
    )


def test_bib_convert_book_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @book{Key1234,
      author = {Some Author},
      title = {Some Title},
      publisher = {Some Publisher},
      year = {1234},
      isbn = {978-1234567890},
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">Some Author: '
        "<em>Some Title</em> Some Publisher, 1234, 978-1234567890.</span>" in html
    )


def test_bib_convert_edited_book_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @book{Key1234,
      editor = {A. N. Editor},
      title = {Some Title},
      publisher = {Some Publisher},
      year = {1234},
      isbn = {978-1234567890},
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">A. N. Editor (ed.): '
        "<em>Some Title</em> Some Publisher, 1234, 978-1234567890.</span>" in html
    )


def test_bib_convert_incollection_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @incollection{Key1234,
      author = {Some Author},
      title = {Some Article},
      editor = {A B and C D and E F},
      publisher = {Some Publisher},
      booktitle = {Some Book},
      year = {1234}
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">Some Author: "Some Article". '
        "In A B, C D, and E F (ed.): <em>Some Book</em>, Some Publisher, 1234." in html
    )


def test_bib_convert_inproceedings_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @inproceedings{Key1234,
      author = {Some Author},
      title = {Some Article},
      booktitle = {Some Book},
      year = {1234},
      doi = {12.3456/78.90},
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">Some Author: "Some Article". '
        "In <em>Some Book</em>, 1234, "
        '<a href="https://doi.org/12.3456/78.90">12.3456/78.90</a>.</span>' in html
    )


def test_bib_convert_misc_to_html(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @misc{Key1234,
      author = {Some Author},
      title = {Some Article},
      year = {1234},
      url = {http://some.where}
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">Some Author: "Some Article" '
        '<a href="http://some.where">http://some.where</a>, '
        "viewed 1234.</span>" in html
    )


def test_bib_convert_missing_year(fs, caplog):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @misc{Key1234,
      author = {Some Author},
      title = {Some Article},
      url = {http://some.where}
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    with caplog.at_level(logging.DEBUG):
        html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">Some Author: "Some Article" '
        '<a href="http://some.where">http://some.where</a>.' in html
    )
    assert len(caplog.record_tuples) == 1
    assert "Bibliography entry missing year" in caplog.record_tuples[0][2]


def test_bib_convert_missing_url(fs):
    fs.create_file(
        "test.bib",
        contents=dedent(
            """\
    @misc{Key1234,
      author = {Some Author},
      title = {Some Article},
      year = {1234}
    }
    """
        ),
    )
    config = Config(bib="test.bib")
    load_bib(config)
    html = bib_to_html(config)
    assert '<p id="Key1234" class="bib">' in html
    assert '<span class="bibkey">Key1234</span>' in html
    assert (
        '<span class="bibentry">Some Author: "Some Article", viewed 1234.</span>'
        in html
    )
