"""Test snippet inclusion."""

import logging
from textwrap import dedent

from mccole.accounting import Info
from mccole.include import inclusion_to_html


def test_include_text_with_badly_formatted_spec(caplog):
    info = Info(src="./page.md")
    spec = '  whatever="a.txt" '
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == ""
    assert len(caplog.record_tuples) == 1
    assert "Unrecognized inclusion spec" in caplog.record_tuples[0][2]


def test_include_text_file_when_file_exists(fs):
    info = Info(src="./page.md")
    spec = '  file="a.txt" '
    fs.create_file("a.txt", contents="AAA")
    html = inclusion_to_html(info, spec, None)
    assert html == '<pre title="a.txt"><code class="language-txt">AAA\n</code></pre>\n'


def test_include_text_file_when_file_missing(fs, caplog):
    info = Info(src="./page.md")
    spec = 'file="a.txt"'
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == "MISSING"
    assert len(caplog.record_tuples) == 1
    assert "Unable to read inclusion" in caplog.record_tuples[0][2]


def test_include_keep_subset_correct(fs):
    info = Info(src="./page.md")
    content = dedent(
        """\
    goes
    // [stays]
    should
    // [/stays]
    goes
    """
    )
    fs.create_file("a.txt", contents=content)
    spec = ' file="a.txt" keep="stays"'
    html = inclusion_to_html(info, spec, None)
    assert (
        html == '<pre title="a.txt"><code class="language-txt">should\n</code></pre>\n'
    )


def test_include_keep_subset_field_in_wrong_order(fs, caplog):
    info = Info(src="./page.md")
    content = "AAA"
    fs.create_file("a.txt", contents=content)
    spec = 'keep="stays" file="a.txt"'
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == ""
    assert len(caplog.record_tuples) == 1
    assert "Unrecognized inclusion spec" in caplog.record_tuples[0][2]


def test_include_omit_subset_correct(fs):
    info = Info(src="./page.md")
    content = dedent(
        """\
    stays
    // [skip]
    should not appear
    // [/skip]
    stays
    """
    )
    fs.create_file("a.txt", contents=content)
    spec = ' file="a.txt" omit="skip"'
    html = inclusion_to_html(info, spec, None)
    assert (
        html
        == '<pre title="a.txt"><code class="language-txt">stays\nstays\n</code></pre>\n'
    )


def test_include_omit_subset_field_in_wrong_order(fs, caplog):
    info = Info(src="./page.md")
    content = "AAA"
    fs.create_file("a.txt", contents=content)
    spec = 'omit="stays" file="a.txt"'
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == ""
    assert len(caplog.record_tuples) == 1
    assert "Unrecognized inclusion spec" in caplog.record_tuples[0][2]


def test_include_keep_omit_subset_correct(fs):
    info = Info(src="./page.md")
    content = dedent(
        """\
    goes
    // [yes]
    should
    // [no]
    should not
    // [/no]
    // [/yes]
    goes
    """
    )
    fs.create_file("a.txt", contents=content)
    spec = ' file="a.txt"   keep="yes"\tomit="no"'
    html = inclusion_to_html(info, spec, None)
    assert (
        html == '<pre title="a.txt"><code class="language-txt">should\n</code></pre>\n'
    )


def test_include_multi_correct(fs):
    info = Info(src="./page.md")
    fs.create_file("a.out", contents="OUT")
    fs.create_file("a.py", contents="PY")
    fs.create_file("a.sh", contents="RUN")
    spec = ' pat="a.*" fill="py sh out" '
    html = inclusion_to_html(info, spec, None)
    for (s, b) in (("py", "PY"), ("sh", "RUN"), ("out", "OUT")):
        expected = f'<pre title="a.{s}"><code class="language-{s}">{b}\n</code></pre>'
        assert expected in html


def test_keep_when_opening_tag_missing(fs, caplog):
    info = Info(src="./page.md")
    content = dedent(
        """\
    goes
    // missing opening tag
    should appear
    // [/stays]
    goes
    """
    )
    fs.create_file("a.txt", contents=content)
    spec = ' file="a.txt" keep="stays"'
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == '<pre title="a.txt"><code class="language-txt">\n</code></pre>\n'
    assert len(caplog.record_tuples) == 1
    assert "Failed to match inclusion 'keep' key" in caplog.record_tuples[0][2]


def test_keep_when_closing_tag_missing(fs, caplog):
    info = Info(src="./page.md")
    content = dedent(
        """\
    goes
    // [stays]
    should appear
    // missing closing tag
    goes
    """
    )
    fs.create_file("a.txt", contents=content)
    spec = ' file="a.txt" keep="stays"'
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == '<pre title="a.txt"><code class="language-txt">\n</code></pre>\n'
    assert len(caplog.record_tuples) == 1
    assert "Failed to match inclusion 'keep' key" in caplog.record_tuples[0][2]


def test_omit_when_opening_tag_missing(fs, caplog):
    info = Info(src="./page.md")
    content = dedent(
        """\
    stays
    // missing opening tag
    should not appear
    // [/no]
    stays
    """
    )
    fs.create_file("a.txt", contents=content)
    spec = ' file="a.txt" omit="stays"'
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == '<pre title="a.txt"><code class="language-txt">\n</code></pre>\n'
    assert len(caplog.record_tuples) == 1
    assert "Failed to match inclusion 'omit' key" in caplog.record_tuples[0][2]


def test_omit_when_closing_tag_missing(fs, caplog):
    info = Info(src="./page.md")
    content = dedent(
        """\
    stays
    // [no]
    should not appear
    // missing closing tag
    stays
    """
    )
    fs.create_file("a.txt", contents=content)
    spec = ' file="a.txt" omit="stays"'
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == '<pre title="a.txt"><code class="language-txt">\n</code></pre>\n'
    assert len(caplog.record_tuples) == 1
    assert "Failed to match inclusion 'omit' key" in caplog.record_tuples[0][2]


def test_include_keep_omit_closing_out_of_order(fs, caplog):
    info = Info(src="./page.md")
    content = dedent(
        """\
    goes
    // [yes]
    should appear
    // [no]
    should not appear
    // [/yes]
    // [/no]
    goes
    """
    )
    fs.create_file("a.txt", contents=content)
    spec = ' file="a.txt"   keep="yes"\tomit="no"'
    with caplog.at_level(logging.WARNING):
        html = inclusion_to_html(info, spec, None)
    assert html == '<pre title="a.txt"><code class="language-txt">\n</code></pre>\n'
    assert len(caplog.record_tuples) == 1
    assert "Failed to match inclusion 'omit' key" in caplog.record_tuples[0][2]
