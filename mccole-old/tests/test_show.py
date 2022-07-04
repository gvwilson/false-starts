"""Test built-i display."""

from types import SimpleNamespace as SN

from mccole.accounting import Config, CrossRef, Info, Seen
from mccole.show import show


def test_show_bib(capsys):
    options = SN(show=["bib"])
    config = Config(bib_data=[{"ID": "left"}, {"ID": "right"}])
    xref = CrossRef()
    seen = Seen(cite={"right"})
    show(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Bibliography keys",
        "- left",
        "+ right"
    ]
    assert captured.out.strip().split("\n") == expected


def test_show_gloss(capsys):
    options = SN(show=["gloss"])
    config = Config(gloss_data=[{"key": "left"}, {"key": "right"}])
    xref = CrossRef()
    seen = Seen(gloss_ref={"right"})
    show(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Glossary keys",
        "- left",
        "+ right"
    ]
    assert captured.out.strip().split("\n") == expected


def test_show_index(capsys):
    options = SN(show=["index"])
    config = Config()
    xref = CrossRef()
    seen = Seen(index_ref={"delta!epsilon", "alpha", "zeta;eta!theta;kappa", "beta;gamma"})
    show(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Index:",
        "- alpha",
        "- beta",
        "- delta",
        "  - epsilon",
        "- eta",
        "  - theta",
        "- gamma",
        "- kappa",
        "- zeta"
    ]
    assert captured.out.strip().split("\n") == expected


def test_show_pages(capsys):
    options = SN(show=["pages"])
    config = Config(pages=[
        Info(
            slug="alpha",
            major="1",
            title="First",
            src="alpha/index.md",
            dst="docs/alpha/index.html"
        ),
        Info(
            slug="beta",
            major="1",
            title="Second",
            src="beta/index.md",
            dst="docs/beta/index.html"
        )
    ])
    xref = CrossRef()
    seen = Seen()
    show(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Pages:",
        "- slug: alpha",
        "  major: 1",
        "  title: First",
        "  src: alpha/index.md",
        "  dst: docs/alpha/index.html",
        "- slug: beta",
        "  major: 1",
        "  title: Second",
        "  src: beta/index.md",
        "  dst: docs/beta/index.html"
    ]
    assert captured.out.strip().split("\n") == expected


def test_show_xref(capsys):
    options = SN(show=["xref"])
    config = Config()
    xref = CrossRef(
        fig_id_to_index={"fig-a": (2, 1)},
        fig_id_to_slug={"fig-a": "topic"},
        hd_id_to_index={"topic": (2,)},
        hd_id_to_slug={"topic": "topic"},
        hd_id_to_title={"topic": "The Topic"},
        hd_index_to_id={(2,): "topic"},
        tbl_id_to_index={},
        tbl_id_to_slug={}
    )
    seen = Seen()
    show(options, config, xref, seen)
    captured = capsys.readouterr()
    expected = [
        "Cross-references",
        "- fig_id_to_index",
        "  - fig-a: (2, 1)",
        "- fig_id_to_slug",
        "  - fig-a: topic",
        "- hd_id_to_index",
        "  - topic: (2,)",
        "- hd_id_to_slug",
        "  - topic: topic",
        "- hd_id_to_title",
        "  - topic: The Topic",
        "- hd_index_to_id",
        "  - (2,): topic",
        "- tbl_id_to_index",
        "- tbl_id_to_slug",
    ]
    assert captured.out.strip().split("\n") == expected
