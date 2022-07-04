import argparse
import re
import sys
import time

import requests

# Match package URL in main index page.
RE_PACKAGE = re.compile(r'<a href="(.+?)">')

# Match release URL in package index page.
RE_RELEASE = re.compile(r'<a href=".+?">(.+?)</a>')

# PyPI domain.
DOMAIN = "https://pypi.org"


def main():
    """Main driver."""
    options = parse_args()
    main_page = get_page(f"{DOMAIN}/simple/", True)
    package_urls = get_package_urls(main_page)
    progress = report_progress(options, len(package_urls))

    for package in package_urls:
        name = get_package_name(package)
        if skip_package(options, name):
            continue
        count = get_package_count(package)
        print(f"{name},{count}")
        progress = report_progress(options, progress, name)


def get_package_count(package):
    """Get the package page and extract count or NA."""
    url = f"{DOMAIN}{package}"
    page = get_page(url)
    if not page:
        print(f"Cannot get {url}", file=sys.stderr)
        return "NA"
    return len(RE_RELEASE.findall(page))


def get_package_name(package_url):
    """Extract package name from URL."""
    return package_url.strip("/").split("/")[-1]


def get_package_urls(page):
    """Extract package URLs from main page."""
    return RE_PACKAGE.findall(page)


def get_page(url, required=False):
    """Get a page; fail if required but not available."""
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    assert not required, f"Unable to get {url}: {resp.status_code}"
    return None


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--after", help="Start recording after this package")
    parser.add_argument("--verbose", action="store_true", help="Report progress")
    return parser.parse_args()


def report_progress(options, arg, name=None):
    """Report progress and update."""
    # Initializing with total package count.
    if isinstance(arg, int):
        return {"expected": arg, "seen": 0, "start": time.time()}

    assert isinstance(arg, dict), "Expected int or dict"
    arg["seen"] += 1
    elapsed = time.time() - arg["start"]
    t_per_package = elapsed / arg["seen"]
    remaining = (arg["expected"] - arg["seen"]) * t_per_package
    if options.verbose:
        print(
            f"{name} {arg['seen']} @ {elapsed:.1f} => {remaining:.1f}",
            file=sys.stderr,
        )
    return arg


def skip_package(options, name):
    """Should we skip this package?"""
    return (options.after is not None) and (name <= options.after)


if __name__ == "__main__":
    main()
