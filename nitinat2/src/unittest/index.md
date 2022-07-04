---
title: "Unit Testing"
---

-   How to test the data download script?
    -   Relies on command-line arguments
    -   Takes several hours to run
    -   Don't know what the output is supposed to be
    -   Output depends on pages that change outside our control
    -   Output is going to screen
-   And how much testing is actually needed?
    -   Wouldn't test as thoroughly as shown here for a one-off
    -   But would if it is going to be used in production by other people
-   Simplest function is `skip_package`
    -   But even that relies on the options returned by `argparse`
    -   Which are stored in a `Namespace` object
    -   We can construct one ourselves

```{.python title="tests/test_download.py"}
from argparse import Namespace

def test_skip_package_after_not_specified():
    options = Namespace(after=None, verbose=False)
    assert not skip_package(options, "something")
```
```bash
$ pytest
collected 2 items
tests/test_download.py .
tests/test_heartbeat.py .
```

-   Could repeat the `Namespace` constructor in every test
-   Or create a [% g fixture "fixture" %] that pytest will construct automatically
    -   Use the `pytest.fixture` [% g decorator "decorator" %] to define a function
    -   Use the function name as a parameter to a unit test
    -   pytest notices that the parameter has the same name as a fixture and calls the function
-   Call the fixture `download_options` because `options` is a very generic name

```{.python title="tests/test_download.py"}
@pytest.fixture
def download_options():
    """Default download_options from argparse."""
    return Namespace(after=None, verbose=False)
```

-   Use this in some tests

```{.python title="tests/test_download.py"}
def test_skip_package_name_before_specified(download_options):
    download_options.after = "b"
    assert skip_package(download_options, "a")


def test_skip_package_name_after_specified(download_options):
    download_options.after = "b"
    assert not skip_package(download_options, "z")


def test_skip_package_name_equal_specified(download_options):
    download_options.after = "b"
    assert skip_package(download_options, "b")
```

-   Some people object to modifying fixtures in this way
    -   A fixture is supposed to be fixed, which reduces cognitive load
    -   If the fixture needs to vary, use a helper function
-   Next step is to test some of the downloading functions
    -   These rely on an HTTP response object from the requests package
    -   More specifically, these rely on that object having two members `status_code` and `text`
-   It's a bit of a cheat to build a `Namespace` object
    -   Could define a `dataclass` or a `namedtuple`
    -   But [Occam's Razor][occams_razor] applies: do not multiply entities (or in this case tools) unnecessarily
-   We'll call a function when we need it rather than creating a fixture

```{.python title="tests/test_download.py"}
def response(status_code=200, text=""):
    """Create an HTTP response object to be filled in."""
    return Namespace(status_code=status_code, text=text)
```

-   Now use it

```{.python title="tests/test_download.py"}
from unittest.mock import patch

def test_get_page_ok():
    resp = response(text="expected")
    with patch("nitinat.download.requests.get", return_value=resp):
        assert get_page("http://somewhere/") == "expected"
```

-   `patch` takes the dotted path to the specific use of the function or method we want to replace and the value we want to return
-   Replaces the named thing with a [% g mock_object "mock object" %]
-   When `get_page` runs, the function `requests.test` in `nitinat.download` is intercepted and our response returned
    -   The URL we give to `get_page` doesn't matter because the real `get_page` isn't called
-   If the main page is unavailable, the program is supposed to throw an exception
    -   Not testing that the error handling does what it's supposed to is a major source of failure in production systems [% b Yuan2015 %]
-   Use `pytest.raises` and specify the expected class of the exception
    -   Could patch inside the exception check
    -   Pick one order and be consistent

```{.python title="tests/test_download.py"}
def test_get_page_fail_when_required_but_not_found():
    resp = response(status_code=404)
    with patch("nitinat.download.requests.get", return_value=resp):
        with pytest.raises(AssertionError):
            get_page("http://somewhere/", True)
```

-   Sub-pages should return `None` instead of failing

```{.python title="tests/test_download.py"}
def test_get_page_succed_when_not_required_and_not_found():
    resp = response(status_code=404)
    with patch("nitinat.download.requests.get", return_value=resp):
        assert get_page("http://somewhere/") == None
```

-   Download program sends its output to the screen
-   pytest provides a fixture called `capsys` that captures `stdout` and `stderr`
-   Test the entire program
    -   Patch `parse_args` to inject the options we want instead of parsing command-line arguments
    -   Intercept `requests.get` to return an empty page
    -   Ask `capsys` for the output seen so far
    -   Check that only the column titles are present

```{.python title="tests/test_download.py"}
def test_no_packages_when_index_page_empty(capsys, download_options):
    resp = response()
    with patch("nitinat.download.parse_args", return_value=download_options):
        with patch("nitinat.download.requests.get", return_value=resp):
            main()
            captured = capsys.readouterr()
            assert captured.out == "Package,Releases\n"
```

-   Simulate a main page that has one package page
    -   Write the URLs that our regular expressions are supposed to catch
    -   Alternative would be to patch `get_package_urls`
    -   Our decision to get the sub-page and extract the count in a single function `get_package_count` now looks short-sighted
-   If the mock object created by `patch` needs to return two or more values, use `side_effect=[...]`
-   Another reason to write a `response` function instead of using a fixture: we need several responses in order for some tests

```{.python title="tests/test_download.py"}
def test_count_single_missing_package(capsys, download_options):
    main_resp = response(text='<a href="alpha">ALPHA</a>')
    page_resp = response(status_code=404, text="")
    with patch("nitinat.download.parse_args", return_value=download_options):
        with patch("nitinat.download.requests.get", side_effect=[main_resp, page_resp]):
            main()
            captured = capsys.readouterr()
            assert captured.out == "Package,Releases\nalpha,NA\n"
```

-   For longer pieces of text, use `textwrap.dedent` to un-indent a block of text inline
    -   The backslash after the opening `"""` ensures that we don't accidentally introduce an opening newline character

```{.python title="tests/test_download.py"}
from textwrap import dedent

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
```

-   Reading the fixtures and expected output from files looks simpler

```{.python title="tests/test_download.py"}
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
```

-   But this doesn't work
    -   When pytest runs, its [% g cwd "current working directory" %] is the project's root directory
    -   So the process looks there for the files
-   Could write the paths `"tests/single_package_main_page.txt"`
    -   But large projects put test files in sub-directories of `tests`
    -   And we don't want to have to rewrite all the tests when we do that
-   Mark the first attempt as "expected to fail"
    -   Can also mark with `pytest.mark.skip` if skipping temporarily

```{.python title="tests/test_download.py"}
@pytest.mark.xfail
def test_single_package_multiple_releases_file(capsys, download_options):
    ...as before...
```

-   Write a helper function to read a file from whatever directory the caller is in
    -   The special variable `__file__` holds the full path of the current file
    -   Its parent is the directory that contains it
    -   So the complicated `Path` expression gets a file from the directory of the source file making the call

```{.python title="tests/test_download.py"}
def local_file(filename):
    path = Path(__file__).parent.joinpath(filename)
    return open(path, "r").read()
```

-   Rewrite the test

```{.python title="tests/test_download.py"}
def test_single_package_multiple_releases_fixed(capsys, download_options):
    main_text = local_file("single_package_main_page.txt")
    page_text = local_file("single_package_sub_page.txt")
    expected = local_file("single_package_expected.txt")
    ...as before...
```

-   This works, but if there are dozens of tests with different fixtures, coming up with filenames will be a headache
    -   So will understanding which files are used in which tests
    -   And maintaining them
-   Embedding the test data in the test file is the better choice in this case
    -   But if your test fixture really needs to be a thousand lines long, the balance tips
