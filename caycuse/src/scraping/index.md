---
title: "Web Scraping"
---

-   The steps in most data analysis projects are:
    1.  Find data
    2.  Collect it
    3.  Tidy it
    4.  Do calculations
    5.  Report results
-   To illustrate Step 2, let's find out how many versions of Python packages there are

## Getting the Data

-   Data source is the simple [PyPI][pypi] package index page <https://pypi.org/simple/>
    -   Has HTML links to one page per package
-   Each package's page has links to released versions in various formats
    -   Over 200K entries
-   Some redundancy, e.g., [% g wheel "wheels" %] and [% g gzip "gzip'd" %] [% g tar "tar" %] files
    -   We have to decide whether to count these separately or fold them together
    -   Every statistical result is the product of many decisions
    -   Different decisions produce different results
-   Use the [`requests`][requests] library to get page
-   The HTML is very highly structured (machine-generated),
    so we can extract fields using [% g regular_expression "regular expressions" %]
    -   [This is a sin][regular_expressions_html]
    -   Look at better ways in [% x website %]

```{.python title="get-release-counts-naive.py"}
import re

import requests

# Match package URL in main index page.
RE_PACKAGE = re.compile(r'<a href="(.+?)">')

# Match release URL in package index page.
RE_RELEASE = re.compile(r'<a href=".+?">(.+?)</a>')

# PyPI domain.
DOMAIN = "https://pypi.org"


index_response = requests.get(f"{DOMAIN}/simple/")
print("Package,Releases")
all_packages = RE_PACKAGE.findall(index_response.text)
for package in all_packages:
    name = package.strip("/").split("/")[-1]
    url = f"{DOMAIN}{package}"
    package_response = requests.get(url)
    count = len(RE_RELEASE.findall(package_response.text))
    print(f"{name},{count}")
```

-   Not a friendly program
-   If several thousand people run this program at the same time it will slow PyPI down
-   Unlikely in this case,
    but a school could easily wind up being [% g blacklisting "blacklisted" %]
    if a hundred students are grabbing data at the same time
-   Popular data sources have to manage floods of requests
-   Programs should [% g throttle "throttle" %] their own activity

## Looking at Data

-   Look at a few [% g summary_statistics "summary statistics" %]

```{.python title="summary-statistics.py"}
import sys

import pandas as pd

datafile = sys.argv[1]
packages = pd.read_csv(datafile)
print(packages["Releases"].agg(["mean", "median", "var", "std", "min", "max"]))
```
```sh
python version-statistics.py release-count.csv
```
```txt
mean         15.967889
median        4.000000
var        6446.184438
std          80.288134
min           0.000000
max       16187.000000
Name: Releases, dtype: float64
```

-   Half of all packages have had fewer than four releases
-   The mean is only slightly higher (1/5 of a [% g stdev "standard deviation" %])
-   And yeah, a package with more than 16,000 releases will pull things up
    -   Cryptocurrency package might be using releases as ledger updates
-   Use a [% g histogram "histogram" %] to show the distribution of values
    -   Its shape (and hence our interpretation) depends on how we [% g bin "bin" %] the data

```{.python title="version-histogram.py"}
import sys
import pandas as pd
import plotly.express as px

datafile = sys.argv[1]
packages = pd.read_csv(datafile)

print('Distribution of Releases')
print(packages.groupby('Releases').count())
print(f'{packages["Releases"].isna().sum()} missing values')

fig = px.histogram(packages, x='Releases', nbins=100, log_y=True, width=600, height=400)
fig.show()
fig.write_image('release-count.svg')
```
```sh
python version-histogram.py release-count.csv
```
```txt
Distribution of Releases
          Package
Releases         
0.0         11721
1.0         33992
2.0         32829
3.0         14999
4.0         18339
5.0          8946
...
4505.0          1
5133.0          1
6460.0          1
10797.0         1

[561 rows x 1 columns]
14 missing values
```

[% figure
   slug="release-count"
   img="release-count.svg"
   caption="Release Count"
   alt="Histogram showing number of releases per package from PyPI."
%]

-   Printed output includes the value for packages with zero releases
-   But does the histogram?
    -   What does Plotly do with `log(0)`?
-   Let's try:

```{.python title="version-histogram.py"}
slice = packages[packages['Releases'] < 100]
fig = px.histogram(slice, x='Releases', nbins=100, log_y=True, width=600, height=400)
fig.show()
fig.write_image('release-count-low.svg')
```

[% figure
   slug="release-count-low"
   img="release-count-low.svg"
   caption="Release Count (Low End)"
   alt="Histogram showing low end of releases per package from PyPI."
%]

-   It seems to include zero
-   But that double-stepping looks weird
-   Is it a plotting artifact or a result of double-counting packages that are released in multiple formats?
    -   To answer that question, we'll need to clean up our data...
-   But first, use a [% g violin_plot "violin plot" %] to get a better feel for the shape of the data

```{.python title="version-other-plots.py"}
datafile = sys.argv[1]
packages = pd.read_csv(datafile)
slice = packages[packages['Releases'] < 100]
fig = px.violin(slice, y='Releases', width=600, height=400)
fig.show()
fig.write_image('release-count-violin.svg')
```

[% figure
   slug="release-count-violin"
   img="release-count-violin.svg"
   caption="Violin Plot (Low End)"
   alt="Violin plot showing almost all packages have just a few releases."
%]

-   Can also use a [% g box_and_whisker_plot "box-and-whisker plot" %]
    -   Lines show minimum, first [% g quartile "quartile" %], median, third quartile, and maximum
    -   Box shows first quartile to third quartile (so half the data lies inside the box)
-   Distance from first quartile to third quartile is the [% g iqr "inter-quartile range" %]
    -   Lower and upper lines cut off at 1.5\\( \times \\)IQR
    -   Anything beyond that is considered an outlier and shown as a point

```{.python title="version-other-plots.py"}
fig = px.box(slice, y='Releases', width=600, height=400)
fig.show()
fig.write_image('release-count-box.svg')
```

[% figure
   slug="release-count-box"
   img="release-count-box.svg"
   caption="Box-and-Whisker Plot (Low End)"
   alt="Box-and-whisker plot showing almost all packages have just a few releases"
%]

## Actually Getting Data

-   First run of the script shown earlier crashed after a few minutes because of a missing sub-page
-   So add a check on the HTTP status codes from queries
    -   Record [% g na "`NA`" %] for those pages
    -   And hope that analysis software interprets this as "not available"
        rather than Namibia or the element sodium
-   Whole thing took about 8.5 hours
    -   So we add a [% g restart "restart" %] capability
-   And those options should be documented
-   Time for [% g taschuks_rules "Taschuk's Rules" %] [% b Taschuk2017 %]:
    1.  Use version control.
    1.  Document your code and usage
    1.  Make common operations easy to control.
    1.  Version your releases.
    1.  Reuse software (within reason)
    1.  Rely on build tools and package managers for installation.
    1.  Do not require root or other special privileges to install or run.
    1.  Eliminate hard-coded paths.
    1.  Include a small test set that can be run to ensure the software is actually working.
    1.  Produce identical results when given identical inputs.
-   And Koch's Amendment: make long-running programs restartable
-   Divide the download script into pieces
    -   Human beings can only keep \\( 7 \pm 2 \\) things in working memory at once
    -   Makes testing easier ([% x unittest %])
-   Write the [% g main_driver "main driver" %] first
    -   Designing top-down
    -   Toward a more-or-less understood goal
-   Read the code aloud to see if it's at a consistent level [% b Wilson2022 %]

```{.python title="get-release-counts-robust.py"}
import argparse
import re
import sys
import time

import requests

# ...regular expression patterns...

def main():
    """Main driver."""
    options = parse_args()
    main_page = get_page(f"{DOMAIN}/simple/", True)
    package_urls = get_package_urls(main_page)
    progress = report_progress(options, len(package_urls))

    print("Package,Releases")
    for package in package_urls:
        name = get_package_name(package)
        if skip_package(options, name):
            continue
        count = get_package_count(package)
        print(f"{name},{count}")
        progress = report_progress(options, progress, name)


# ...function definitions...


if __name__ == "__main__":
    main()
```

-   Put the functions in alphabetical order
    -   There may be a "logical" order...
    -   ...but as soon as there are utilities called by more than one other function,
        you're trying to linearize a directed graph
    -   Findability reduces [% g cognitive_load "cognitive load" %] [% b Hermans2021 %]
-   But write the functions in that logical order
    -   Because you are tracing execution in your head as you code
-   Handle command-line arguments using [`argparse`][argparse]
-   `--verbose` to turn on reporting
-   <code>--after <em>name</em></code> rather than "start with name"
    because all you can be sure of is the last thing you saw
    -   Better implementation would read the last line of the data already downloaded
        and restart from there

```{.python title="get-release-counts-robust.py"}
def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--after", help="Start recording after this package")
    parser.add_argument("--verbose", action="store_true", help="Report progress")
    return parser.parse_args()
```

-   Get a page
    -   "Just" a wrapper around `requests.get`
    -   But testing is easier if we only have one thing to replace
    -   And wrapping it ensures consistent error handling
-   Allow for the fact that the main page is required but package pages are not

```{.python title="get-release-counts-robust.py"}
def get_page(url, required=False):
    """Get a page; fail if required but not available."""
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    assert not required, f"Unable to get {url}: {resp.status_code}"
    return None
```

-   Get the package count from the main page
    -   This could have been left inline, but it sounded off-level when read aloud
-   Get the package count or `NA` from a package page
    -   `main` doesn't need to know we're handling this specially

```{.python title="get-release-counts-robust.py"}
def get_package_urls(page):
    """Extract package URLs from main page."""
    return RE_PACKAGE.findall(page)

def get_package_count(package):
    """Get the package page and extract count or NA."""
    url = f"{DOMAIN}{package}"
    page = get_page(url)
    if not page:
        print(f"Cannot get {url}", file=sys.stderr)
        return "NA"
    return len(RE_RELEASE.findall(page))
```

-   Went back and forth on whether this should be `skip_package` or `process_package`
    -   I.e., is the code more naturally "do this" or "don't do that"?
-   Another option would have been `handle_package` in `main` and to shorten the loop

```{.python title="get-release-counts-robust.py"}
def skip_package(options, name):
    """Should we skip this package?"""
    return (options.after is not None) and (name <= options.after)
```

-   Reporting progress is actually the most complex part of this code
    -   Keeping track requires several bits of information,
        so put them in a dictionary instead of passing around three variables
    -   Call `report_progress` with `None` to initialize that dictionary
    -   Call it with a dictionary to update and report
    -   "Initialize or use" is a common [% g design_pattern "design pattern" %]

```{.python title="get-release-counts-robust.py"}
def report_progress(options, arg, name=None):
    """Report progress and update."""
    # Initializing with total package count.
    if isinstance(arg, int):
        return {"expected": arg, "seen": 0, "start": time.time()}

    assert isinstance(arg, dict), f"Expected int or dict"
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
```

-   Now for a little interactive testing

```bash
$ python get-release-counts-robust.py
0,1
0-0,0
00000a,1
0-0-1,1
^C
```

-   Does the verbose flag work?

```bash
$ python get-release-counts-robust.py --verbose
0,1
0 1 @ 0.1 => 52028.1
0-0,0
0-0 2 @ 0.3 => 58556.5
^C
```

-   Easier to see if we redirect `stdout` to `/dev/null`

```bash
$ python get-release-counts-robust.py --verbose > /dev/null
0 1 @ 0.2 => 55858.6
0-0 2 @ 0.3 => 56518.2
00000a 3 @ 0.5 => 56123.8
^C
```

-   Start after some package?


```bash
$ python get-release-counts-robust.py --verbose --after pytest > /dev/null
pytest123 1 @ 0.3 => 104411.9
pytest2md 2 @ 0.5 => 87620.0
pytest30 3 @ 0.6 => 79357.2
^C
```

-   This code is more than three times as long as the original
-   But it will be easier for the next person (including our future self) to understand
-   And it's going to be a lot easier to test,
    because we don't want to be testing by hand as the code evolves
