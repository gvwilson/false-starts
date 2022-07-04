"""Test glossary."""

import logging
import re
from textwrap import dedent

import pytest
import yaml

from mccole.accounting import Config, Seen
from mccole.gloss import GlossaryEntry, gloss_to_html, load_gloss
from mccole.util import McColeExc


@pytest.fixture
def triple_raw():
    return yaml.safe_load(
        dedent(
            """\
        - key: first
          en:
            term: first term
            def: >
              First definition
          fr:
            term: premiere mot
            def: >
              Premiere definition
        - key: second
          ref:
          - first
          en:
            term: second term
            def: >
              Second definition
        - key: third
          en:
            term: third term
            def: >
              Third definition [second](#second)
        """
        )
    )


@pytest.fixture
def triple(triple_raw):
    return [GlossaryEntry(e) for e in triple_raw]


def test_gloss_empty_when_not_specified(fs):
    config = Config()
    load_gloss(config)
    assert config.gloss_data == []
    assert config.gloss_keys == set()


def test_gloss_fail_with_nonexistent_file(fs):
    config = Config(gloss="test.yml")
    with pytest.raises(McColeExc):
        load_gloss(config)


def test_gloss_load_empty_file_when_present(fs):
    fs.create_file("test.yml", contents="")
    config = Config(gloss="test.yml")
    load_gloss(config)
    assert config.gloss_data == []
    assert config.gloss_keys == set()


def test_gloss_load_file_containing_data(fs):
    fs.create_file(
        "test.yml",
        contents=dedent(
            """\
            - key: a_term
              en:
                term: term
                def: >
                  The definition
                  on multiple lines.
            """
        ),
    )
    config = Config(gloss="test.yml")
    load_gloss(config)
    assert len(config.gloss_data) == 1
    entry = config.gloss_data[0]
    assert entry.key == "a_term"
    assert entry["en", "term"] == "term"
    assert re.match(
        r"The definition\s+on multiple lines.", entry["en", "def"], re.DOTALL
    )
    assert config.gloss_keys == {"a_term"}


def test_gloss_fails_with_no_language(triple):
    config = Config(gloss_data=triple)
    with pytest.raises(McColeExc):
        gloss_to_html(config, Seen())


def test_gloss_succeeds_with_no_glossary_data():
    config = Config(lang="en")
    assert not gloss_to_html(config, Seen())


def test_gloss_fails_with_missing_key(triple_raw):
    del triple_raw[1]["key"]
    with pytest.raises(McColeExc):
        triple = [GlossaryEntry(e) for e in triple_raw]


def test_gloss_succeeds_with_good_data(triple):
    config = Config(lang="en", gloss_data=triple)
    html = gloss_to_html(config, Seen())
    expected = dedent(
        """\
        <dl>
        <dt><span class="glosskey" id="first">first term</span></dt>
        <dd>First definition</dd>
        <dt><span class="glosskey" id="second">second term</span></dt>
        <dd>Second definition</dd>
        <dt><span class="glosskey" id="third">third term</span></dt>
        <dd>Third definition <a href="#second">second</a></dd>
        </dl>
        """
    )
    assert html.strip() == expected.strip()


def test_gloss_succeeds_with_acronym(triple):
    triple[0]["en", "acronym"] = "ABC"
    config = Config(lang="en", gloss_data=triple)
    html = gloss_to_html(config, Seen())
    assert '<dt><span class="glosskey" id="first">first term</span> (ABC)</dt>' in html


def test_gloss_succeeds_with_valid_ref(triple):
    triple[0]["en", "ref"] = ["second", "third"]
    config = Config(lang="en", gloss_data=triple)
    html = gloss_to_html(config, Seen())
    assert (
        'See also: <a href="#second">second term</a>, <a href="#third">third term</a>.'
        in html
    )


def test_gloss_fails_with_missing_ref(caplog, triple):
    triple[0]["en", "ref"] = ["missing"]
    config = Config(lang="en", gloss_data=triple)
    with caplog.at_level(logging.WARNING):
        gloss_to_html(config, Seen())
    assert len(caplog.record_tuples) == 1
    assert (
        "Bad cross-reference 'missing' in glossary entry"
        in caplog.record_tuples[0][2]
    )
