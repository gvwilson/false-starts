"""Test consistency checks."""

import re
from textwrap import dedent
from types import SimpleNamespace as SN

from mccole.accounting import Config, CrossRef, Info, Seen
from mccole.check import check


def test_check_bib_with_no_problems(capsys):
    options = SN(check=["bib"])
    config = Config(bib_keys={"one", "three"})
    xref = CrossRef()
    seen = Seen(cite={"one", "three"})
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


def test_check_bib_with_unused_keys(capsys):
    options = SN(check=["bib"])
    config = Config(bib_keys={"one", "two", "three"})
    xref = CrossRef()
    seen = Seen(cite={"one", "three"})
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Unused biblography keys:",
        "- two"
    ]
    assert captured.out.strip().split("\n") == expected


def test_check_bib_data_out_of_order(capsys):
    options = SN(check=["bib"])
    config = Config(bib_data=[
        {"ID": "Zabc1234"},
        {"ID": "Aabc1234"},
        {"ID": "Babc1234"},
        {"ID": "Mabc1234"},
        {"ID": "Gabc1234"}
    ])
    xref = CrossRef()
    seen = Seen()
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Bibliography entry Aabc1234 out of order.",
        "Bibliography entry Gabc1234 out of order."
    ]
    assert captured.out.strip().split("\n") == expected


def test_check_bib_data_bad_keys(capsys):
    options = SN(check=["bib"])
    config = Config(bib_data=[
        {"ID": "1234Babc"},
        {"ID": "Aabc12"},
        {"ID": "zabc1234"},
    ])
    xref = CrossRef()
    seen = Seen()
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Badly-formatted bibliography key 1234Babc.",
        "Badly-formatted bibliography key Aabc12.",
        "Badly-formatted bibliography key zabc1234.",
    ]
    assert captured.out.strip().split("\n") == expected


def test_check_code_no_language_specified(capsys):
    options = SN(check=["code"])
    html = dedent('''\
    <pre title="something"><code class=""></code></pre>
    ''')
    config = Config(pages=[Info(html=html, src="filename.txt")])
    xref = CrossRef()
    seen = Seen()
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Code block something in filename.txt has unrecognized class ."


def test_check_code_body_too_long(capsys):
    options = SN(check=["code"])
    html = dedent('''\
    <pre title="something"><code class="language-py">{}</code></pre>
    '''.format("a\n" * 1000))
    config = Config(pages=[Info(html=html, src="filename.txt")])
    xref = CrossRef()
    seen = Seen()
    check(options, config, xref, seen)
    actual = capsys.readouterr().out.strip()
    assert re.search(r"Code block something in filename\.txt has \d+ lines \(> \d+\)\.", actual)


def test_check_code_line_too_long(capsys):
    options = SN(check=["code"])
    html = dedent('''\
    <pre title="something"><code class="language-py">\n{}\n</code></pre>
    '''.format("a" * 1000))
    config = Config(pages=[Info(html=html, src="filename.txt")])
    xref = CrossRef()
    seen = Seen()
    check(options, config, xref, seen)
    actual = capsys.readouterr().out.strip()
    assert re.search(r"Code block something in filename\.txt has \d+ long lines \(> \d+\)\.", actual)


def test_check_gloss_with_no_problems(capsys):
    options = SN(check=["gloss"])
    config = Config(gloss_keys={"alpha", "beta"})
    xref = CrossRef()
    seen = Seen(gloss_ref={"alpha", "beta"})
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


def test_check_gloss_with_unused_entry(capsys):
    options = SN(check=["gloss"])
    config = Config(gloss_keys={"alpha", "beta", "gamma"})
    xref = CrossRef()
    seen = Seen(gloss_ref={"alpha", "beta"})
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Unused glossary keys:",
        "- gamma"
    ]
    assert captured.out.strip().split("\n") == expected


def test_check_gloss_unknown_entry_not_reported(capsys):
    options = SN(check=["gloss"])
    config = Config(gloss_keys={"alpha"})
    xref = CrossRef()
    seen = Seen(gloss_ref={"alpha", "beta"})
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


def test_check_gloss_entries_out_of_order(capsys):
    options = SN(check=["gloss"])
    gloss_data = [
        {"fr": {"key": "alpha", "term": "Alpha"}},
        {"fr": {"key": "gamma", "term": "Gamma"}},
        {"fr": {"key": "beta", "term": "Beta"}},
    ]
    config = Config(lang="fr", gloss_data=gloss_data)
    xref = CrossRef()
    seen = Seen({entry["fr"]["key"] for entry in gloss_data})
    check(options, config, xref, seen)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Glossary entry beta out of order."
