---
title: "Getting a Dataset"
---

-   The steps in most data analysis projects are:
    1.  Find data
    2.  Collect it
    3.  Tidy it
    4.  Do calculations
    5.  Report results
-   To illustrate Step 2, let's find out how many versions of Python packages there are
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

-   Still not a friendly program
    -   If several thousand people run this program at the same time it will slow PyPI down
-   Unlikely in this case,
    but a school could easily wind up being [% g blacklisting "blacklisted" %]
    if a hundred students are grabbing data at the same time
-   Popular data sources have to manage floods of requests
-   Programs should [% g throttle "throttle" %] their own activity
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
