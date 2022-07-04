"""Test main program."""

import logging

from mccole.config import DEFAULT_CONFIG_FILE
from mccole.mccole import main

NO_CHAPTERS = """\
lang: en
chapters:
"""

ONE_CHAPTER = """\
lang: en
chapters:
- slug: first
  title: First
"""


CHAPTER_BIB_GLOSS = """\
lang: en
chapters:
- slug: first
  title: First
bib: _data/bibliography.bib
gloss: _data/glossary.yml
"""


BIBLIOGRAPHY = """\
@misc{Cite1234,
  author = {Some Author},
  title = {The Title},
  year = {1234},
  url = {https://somewhere}
}
"""


GLOSSARY = """\
- key: first
  en:
    term: first term
    def: >
      First definition
"""


FIGURE = """\
---
template: page.html
---
<figure id="short-figure">
  <img src="figures/short.svg" alt="Short caption" />
  <figcaption>Long version of short caption.</figcaption>
</figure>
"""


TABLE = """\
---
template: page.html
---
<div class="table" id="short-table" cap="Short table caption.">
| Left | Right |
| ---- | ----- |
| 1234 | seven |
</div>
"""

PAGE = """\
---
template: page.html
---
text
"""


def test_main_error_message_when_no_config_file(fs, caplog):
    with caplog.at_level(logging.WARNING):
        main([])
    assert len(caplog.record_tuples) == 1


def test_main_no_logging_when_not_enabled(fs, caplog):
    fs.create_file(DEFAULT_CONFIG_FILE, contents=NO_CHAPTERS)
    main([])
    assert len(caplog.record_tuples) == 0


def test_main_delete_output_by_default(fs, caplog):
    fs.create_file("docs/to_delete.txt", contents="to delete")
    fs.create_file(DEFAULT_CONFIG_FILE, contents=ONE_CHAPTER)
    fs.create_file("first/index.md", contents="test")
    main([])
    assert fs.exists("docs/first/index.html")
    assert not fs.exists("docs/to_delete.txt")


def test_main_do_not_delete_output(fs, caplog):
    fs.create_file("docs/to_delete.txt", contents="to delete")
    fs.create_file(DEFAULT_CONFIG_FILE, contents=ONE_CHAPTER)
    fs.create_file("first/index.md", contents="test")
    main(["-k"])
    assert fs.exists("docs/first/index.html")
    assert fs.exists("docs/to_delete.txt")


def test_main_report_unreferenced_figure(fs, caplog):
    fs.create_file(DEFAULT_CONFIG_FILE, contents=ONE_CHAPTER)
    fs.create_file("_template/page.html", contents="")
    fs.create_file("first/index.md", contents=FIGURE)
    with caplog.at_level(logging.WARNING):
        main(["-u"])
    assert len(caplog.record_tuples) == 1
    assert caplog.record_tuples[0][2] == "Unreferenced figure:\n- short-figure"


def test_main_report_unreferenced_table(fs, caplog):
    fs.create_file(DEFAULT_CONFIG_FILE, contents=ONE_CHAPTER)
    fs.create_file("_template/page.html", contents="")
    fs.create_file("first/index.md", contents=TABLE)
    with caplog.at_level(logging.WARNING):
        main(["-u"])
    assert len(caplog.record_tuples) == 1
    assert caplog.record_tuples[0][2] == "Unreferenced table:\n- short-table"


def test_main_do_not_report_unused_citation_glossary_at_low_level(fs, caplog):
    fs.create_file(DEFAULT_CONFIG_FILE, contents=CHAPTER_BIB_GLOSS)
    fs.create_file("_template/page.html", contents="")
    fs.create_file("first/index.md", contents=PAGE)
    fs.create_file("_data/glossary.yml", contents=GLOSSARY)
    fs.create_file("_data/bibliography.bib", contents=BIBLIOGRAPHY)
    with caplog.at_level(logging.WARNING):
        main(["-u"])
    assert len(caplog.record_tuples) == 0


def test_main_show_css(capsys):
    main(["--css"])
    captured = capsys.readouterr()
    assert "/* McCole CSS */" in captured.out


def test_main_show_template_list(capsys):
    main(["--templates"])
    captured = capsys.readouterr()
    assert "page.html" in captured.out
    assert all(s.strip().endswith(".html") for s in captured.out.strip().split("\n"))


def test_main_show_specific_template(capsys):
    main(["--template", "page.html"])
    captured = capsys.readouterr()
    assert "<!DOCTYPE html>" in captured.out


def test_main_show_nonexistent_template(capsys):
    main(["--template", "missing.html"])
    captured = capsys.readouterr()
    assert "Unknown template 'missing.html'" in captured.out
