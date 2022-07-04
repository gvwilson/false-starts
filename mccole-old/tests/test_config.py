"""Test configuration."""

from textwrap import dedent

import pytest

from mccole.config import DEFAULT_CONFIG_FILE, DEFAULTS, load_config
from mccole.template import TEMPLATE_DIR
from mccole.util import McColeExc


def test_config_file_not_found(fs, options):
    with pytest.raises(McColeExc):
        load_config(options)


def test_config_empty_file(fs, options):
    fs.create_file(DEFAULT_CONFIG_FILE, contents="")
    config = load_config(options)
    assert config.src == DEFAULTS["src"]
    assert config.dst == DEFAULTS["dst"]


def test_config_read_links_existing(fs, options):
    links = dedent(
        """\
    - key: mccole
      url: "https://github.com/gvwilson/mccole"
      title: McCole
    """
    )
    fs.create_file(DEFAULT_CONFIG_FILE, contents="links: links.yml")
    fs.create_file("links.yml", contents=links)
    config = load_config(options)
    assert config.links_data == [
        {
            "key": "mccole",
            "url": "https://github.com/gvwilson/mccole",
            "title": "McCole",
        }
    ]


def test_config_read_links_nonexistent(fs, options):
    fs.create_file(DEFAULT_CONFIG_FILE, contents="links: links.yml")
    with pytest.raises(McColeExc):
        load_config(options)


def test_config_override_src(fs, options):
    options.src = "SRC"
    fs.create_file(DEFAULT_CONFIG_FILE, contents="")
    config = load_config(options)
    assert config.src == "SRC"


def test_config_override_dst(fs, options):
    options.dst = "DST"
    fs.create_file(DEFAULT_CONFIG_FILE, contents="")
    config = load_config(options)
    assert config.dst == "DST"


def test_config_templates_empty_if_none_available(fs, options):
    fs.create_file(DEFAULT_CONFIG_FILE, contents="")
    config = load_config(options)
    assert not config.template


def test_config_templates_read_html_only(fs, options):
    fs.create_file(DEFAULT_CONFIG_FILE, contents="")
    for filename in ["a.html", "b.html", "c.txt", "d.html~"]:
        fs.create_file(f"{TEMPLATE_DIR}/{filename}", contents=filename)
    config = load_config(options)
    assert len(config.template) == 2
    for filename in ["a.html", "b.html"]:
        assert config.template[filename] == filename
