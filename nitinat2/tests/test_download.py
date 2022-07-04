"""Test data download script."""

from argparse import Namespace
from pathlib import Path
from textwrap import dedent
from unittest.mock import patch

import pytest

from nitinat.download import get_page, main, skip_package


@pytest.fixture
def download_options():
    """Default download_options from argparse."""
    return Namespace(after=None, verbose=False)


def response(status_code=200, text=""):
    """Create an HTTP response object to be filled in."""
    return Namespace(status_code=status_code, text=text)


def test_skip_package_after_not_specified():
    options = Namespace(after=None, verbose=False)
    assert not skip_package(options, "something")


def test_skip_package_name_before_specified(download_options):
    download_options.after = "b"
    assert skip_package(download_options, "a")


def test_skip_package_name_after_specified(download_options):
    download_options.after = "b"
    assert not skip_package(download_options, "z")


def test_skip_package_name_equal_specified(download_options):
    download_options.after = "b"
    assert skip_package(download_options, "b")


def test_get_page_ok():
    resp = response(text="expected")
    with patch("nitinat.download.requests.get", return_value=resp):
        assert get_page("http://somewhere/") == "expected"


def test_get_page_fail_when_required_but_not_found():
    resp = response(status_code=404)
    with patch("nitinat.download.requests.get", return_value=resp):
        with pytest.raises(AssertionError):
            get_page("http://somewhere/", True)


def test_get_page_succed_when_not_required_and_not_found():
    resp = response(status_code=404)
    with patch("nitinat.download.requests.get", return_value=resp):
        assert get_page("http://somewhere/") is None


def test_no_packages_when_index_page_empty(capsys, download_options):
    resp = response()
    with patch("nitinat.download.parse_args", return_value=download_options):
        with patch("nitinat.download.requests.get", return_value=resp):
            main()
            captured = capsys.readouterr()
            assert captured.out == "Package,Releases\n"


def test_count_single_missing_package(capsys, download_options):
    main_resp = response(text='<a href="alpha">ALPHA</a>')
    page_resp = response(status_code=404, text="")
    with patch("nitinat.download.parse_args", return_value=download_options):
        with patch("nitinat.download.requests.get", side_effect=[main_resp, page_resp]):
            main()
            captured = capsys.readouterr()
            assert captured.out == "Package,Releases\nalpha,NA\n"


def test_count_single_package_single_release(capsys, download_options):
    main_resp = response(text='<a href="alpha">ALPHA</a>')
    page_resp = response(text='<a href="./alpha/1.2.3">Version 1.2.3</a>')
    with patch("nitinat.download.parse_args", return_value=download_options):
        with patch("nitinat.download.requests.get", side_effect=[main_resp, page_resp]):
            main()
            captured = capsys.readouterr()
            assert captured.out == "Package,Releases\nalpha,1\n"


def test_count_single_package_multiple_releases(capsys, download_options):
    main_resp = response(text='<a href="alpha">ALPHA</a>')
    page_resp = response(
        text=dedent(
            """\
    <a href="./alpha/1.2.3">Version 1.2.3</a>
    <a href="./alpha/4.5.6">Version 4.5.6</a>
    <a href="./alpha/7.8.9">Version 7.8.9</a>
    """
        )
    )
    with (
        patch("nitinat.download.parse_args", return_value=download_options),
        patch("nitinat.download.requests.get", side_effect=[main_resp, page_resp]),
    ):
        main()
        captured = capsys.readouterr()
        assert captured.out == dedent(
            """\
        Package,Releases
        alpha,3
        """
        )


@pytest.mark.xfail
def test_single_package_multiple_releases_file(capsys, download_options):
    main_text = open("single_package_main_page.txt", "r").read()
    page_text = open("single_package_sub_page.txt", "r").read()
    expected = open("single_package_expected.txt", "r").read()
    main_resp = response(text=main_text)
    page_resp = response(text=page_text)
    with (
        patch("nitinat.download.parse_args", return_value=download_options),
        patch("nitinat.download.requests.get", side_effect=[main_resp, page_resp]),
    ):
        main()
        captured = capsys.readouterr()
        assert captured.out == expected


def local_file(filename):
    path = Path(__file__).parent.joinpath(filename)
    return open(path, "r").read()


def test_single_package_multiple_releases_fixed(capsys, download_options):
    main_text = local_file("single_package_main_page.txt")
    page_text = local_file("single_package_sub_page.txt")
    expected = local_file("single_package_expected.txt")
    main_resp = response(text=main_text)
    page_resp = response(text=page_text)
    with (
        patch("nitinat.download.parse_args", return_value=download_options),
        patch("nitinat.download.requests.get", side_effect=[main_resp, page_resp]),
    ):
        main()
        captured = capsys.readouterr()
        assert captured.out == expected
