---
title: "Data Science Tools"
---

-   Motivating problem: how big is the average Python package?
-   What do we mean by "big"?
    -   Count lines and characters for now
-   What do we mean by "average"?
    -   Analyze the packages on this computer to start

## Getting Data

-   Where is Python installed?

```py
import sys
print('\n'.join(sys.path))
```
```txt

/Users/gregwilson/conda/envs/nitinat/lib/python39.zip
/Users/gregwilson/conda/envs/nitinat/lib/python3.9
/Users/gregwilson/conda/envs/nitinat/lib/python3.9/lib-dynload
/Users/gregwilson/conda/envs/nitinat/lib/python3.9/site-packages
```

-   The blank at the start is the empty string, which means "current directory"
-   Use the shell to find and display Python file sizes

```sh
find /Users/gregwilson/conda -name '*.py' -exec wc -l -c {} \;
```
```txt
     181    3955 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/number_types.py
      42    1581 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/encode.py
      81    2342 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/compat.py
      43    1669 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/util.py
      18     717 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/__init__.py
      42    1165 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/packer.py
     771   25858 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/builder.py
     129    4708 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/table.py
       9     181 /Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/info/test/run_test.py
      51     905 /Users/gregwilson/conda/pkgs/flatten-dict-0.4.2-pyhd8ed1ab_1/site-packages/flatten_dict/reducers.py
...
```

-   We could convert this output to [% g csv "comma-separated values" %] (CSV)
    with command-line tools like [awk][awk] or [sed][sed]
    -   But since we're using Python anyway...

```{.python title="wc2csv.py"}
import sys

print('Lines,Characters,Path')
for line in sys.stdin:
    fields = line.split()
    print('{},{},{}'.format(*fields))
```

-   Run it as shown below
    -   Break lines to make commands more visible (and to prevent long lines)

```sh
find /Users/gregwilson/conda -name '*.py' -exec wc -l -c {} \; \
  | python wc2csv.py \
  > python-local-package-size.csv
head python-local-package-size.csv
```
```txt
Lines,Characters,Path
181,3955,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/number_types.py
42,1581,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/encode.py
81,2342,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/compat.py
43,1669,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/util.py
18,717,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/__init__.py
42,1165,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/packer.py
771,25858,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/builder.py
129,4708,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/site-packages/flatbuffers/table.py
9,181,/Users/gregwilson/conda/pkgs/python-flatbuffers-1.12-pyhd8ed1ab_1/info/test/run_test.py
...
```

-   This command takes 15 minutes to run and produces 24Mbyte
    -   We're going to want to save the data and re-use it
-   This is [% g tidy_data "tidy data" %]
    1.  Each column contains one statistical variable
        (i.e., one property that was measured or observed)
    2.  Each different observation is in a different row
    3.  There is one table for each set of observations
    4.  If there are multiple tables,
        each table has a column containing a unique [% g key "key" %]
        so that related data can be linked

## Analyzing Tabular Data

-   There's a lot of tabular data in the world
-   People want to do a lot of complex things with it, so Python's tools can be bewildering at first
    1.  Built-in lists and the `array` module
    2.  [NumPy][numpy] provides multidimensional arrays
    3.  [Pandas][pandas] provides [% g dataframe "dataframes" %] with named columns for tidy data
-   We will use a small subset of Pandas
    -   Gives us tables whose columns can have different datatypes
    -   Access columns by name
    -   Access rows by index
-   Load our CSV data into memory and have a look
    -   Only takes a second

```{.python title="pandas-read-display.py"}
import pandas

data = pandas.read_csv('python-local-package-size.csv')
print(data)
```
```txt
        Lines  Characters                                               Path
0         181        3955  /Users/gregwilson/conda/pkgs/python-flatbuffer...
1          42        1581  /Users/gregwilson/conda/pkgs/python-flatbuffer...
2          81        2342  /Users/gregwilson/conda/pkgs/python-flatbuffer...
3          43        1669  /Users/gregwilson/conda/pkgs/python-flatbuffer...
4          18         717  /Users/gregwilson/conda/pkgs/python-flatbuffer...
...       ...         ...                                                ...
213060     35        1875  /Users/gregwilson/conda/share/qt/3rd_party_lic...
213061    143        5056  /Users/gregwilson/conda/share/qt/3rd_party_lic...
213062     62        1948  /Users/gregwilson/conda/share/qt/3rd_party_lic...
213063    171        6228  /Users/gregwilson/conda/share/qt/3rd_party_lic...
213064    112        3924  /Users/gregwilson/conda/share/doc/dbus/example...

[213065 rows x 3 columns]
```

-   The [% g header_row "header row" %] tells us the names of the columns
-   We can get these names using the dataframe's `columns` [% g property "property" %]
    -   Not a method call

```{.python title="pandas-read-display.py"}
print(data.columns)
```
```txt
Index(['Lines', 'Characters', 'Path'], dtype='object')
```

-   Result is an `Index` object containing the columns' names and other information
-   Its `values` property contains just the names

```{.python title="pandas-read-display.py"}
print(data.columns.values)
```
```txt
['Lines' 'Characters' 'Path']
```

-   We normally import Pandas using an [% g alias "alias" %] called `pd`
    to save a few characters of typing and (more importantly) make code a little easier to read
-   Re-load our data that way
    -   And use a more meaningful name than `data`
    -   Then select a column by name

```{.python title="pandas-select-col.py"}
import pandas as pd

packages = pd.read_csv('python-local-package-size.csv')
print(packages['Path'])
```
```txt
0         /Users/gregwilson/conda/pkgs/python-flatbuffer...
1         /Users/gregwilson/conda/pkgs/python-flatbuffer...
2         /Users/gregwilson/conda/pkgs/python-flatbuffer...
3         /Users/gregwilson/conda/pkgs/python-flatbuffer...
4         /Users/gregwilson/conda/pkgs/python-flatbuffer...
                                ...                        
213060    /Users/gregwilson/conda/share/qt/3rd_party_lic...
213061    /Users/gregwilson/conda/share/qt/3rd_party_lic...
213062    /Users/gregwilson/conda/share/qt/3rd_party_lic...
213063    /Users/gregwilson/conda/share/qt/3rd_party_lic...
213064    /Users/gregwilson/conda/share/doc/dbus/example...
Name: Path, Length: 213065, dtype: object
```

-   The line at the end tells us:
    -   The name of the column we selected
    -   How many records there are
    -   The column's data type
-   We can select several columns at once by giving a list of names
    -   Which results in double square brackets
    -   Outer brackets mean "we're selecting something"
    -   Inner ones means "we're providing a list to specify what we're selecting"

```{.python title="pandas-select-col.py"}
print(packages[['Lines', 'Characters']])
```
```txt
        Lines  Characters
0         181        3955
1          42        1581
2          81        2342
3          43        1669
4          18         717
...       ...         ...
213060     35        1875
213061    143        5056
213062     62        1948
213063    171        6228
213064    112        3924

[213065 rows x 2 columns]
```

-   What if we want to select a row?

```{.python title="pandas-select-row-fail.py"}
print(packages[0])
```
```txt
Traceback (most recent call last):
  File "/Users/gregwilson/conda/envs/nitinat/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3621, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 163, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/gregwilson/writing/mesachie/src/dstools/pandas-select-col.py", line 8, in <module>
    print(packages[0])
  File "/Users/gregwilson/conda/envs/nitinat/lib/python3.9/site-packages/pandas/core/frame.py", line 3505, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Users/gregwilson/conda/envs/nitinat/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3623, in get_loc
    raise KeyError(key) from err
KeyError: 0
```

-   Pandas error messages aren't particularly readable
-   Pandas doesn't allow us to select rows by numeric index
    -   Ambiguous, since `1` could mean "first column" rather than "first row"
-   Instead, use a property of the dataframe called `iloc` (for "indexed location")

```{.python title="pandas-select-row-iloc.py"}
print(packages.iloc[0])
```
```txt
Lines                                                       181
Characters                                                 3955
Path          /Users/gregwilson/conda/pkgs/python-flatbuffer...
Name: 0, dtype: object
```

-   Displays a two-column table with keys and values
    -   Count from zero (for [surprising reasons][hoye-count-from-zero])

-   We can use a [% g slice "slice" %] to select multiple rows
    -   <span class="rule">If you're writing a loop to process a table, you're doing something wrong</span>

```{.python title="pandas-select-row-iloc.py"}
print(packages.iloc[0:5])
```
```txt
   Lines  Characters                                               Path
0    181        3955  /Users/gregwilson/conda/pkgs/python-flatbuffer...
1     42        1581  /Users/gregwilson/conda/pkgs/python-flatbuffer...
2     81        2342  /Users/gregwilson/conda/pkgs/python-flatbuffer...
3     43        1669  /Users/gregwilson/conda/pkgs/python-flatbuffer...
4     18         717  /Users/gregwilson/conda/pkgs/python-flatbuffer...
```

-   We can mix names and numbers to select subsections by column and then row
    -   Don't need `iloc` in this case because
        selecting by column gives us back a one-dimensional `Series` object
        that interprets an integer index the way we want

```{.python title="pandas-select-row-iloc.py"}
print(packages['Characters'][0:3])
```
```txt
0    3955
1    1581
2    2342
Name: Characters, dtype: int64
```

-   Can also select by row and then column using `iloc`
    -   But indexing out of order makes code harder to read, so don't do this

```{.python title="pandas-select-row-iloc.py"}
print(packages.iloc[0:3]['Characters'])
```
```txt
0    3955
1    1581
2    2342
Name: Characters, dtype: int64
```

## Visualizing a Dataframe

-   [`matplotlib`][matplotlib] is the most widely used plotting module for Python,
    but is fairly low-level
-   [Plotly Express][plotly] is newer and better suited to creating graphics for browsers
    -   Usually import using the alias `px`
-   Use this to create a simple scatter plot
    -   The figure object's `show` method runs a local server and opens the image in the browser for viewing
    -   Its `write_image` method saves it as a file
    -   We put the generated figure in a `figures` sub-directory to avoid clutter
    -   And use [% g svg "SVG" %] because [% g vector_graphics "vector graphics" %] resizes better than [% g raster_graphics "raster graphics" %]

```{.python title="scatter-lines-characters.py"}
import pandas as pd
import plotly.express as px

packages = pd.read_csv('python-local-package-size.csv')
fig = px.scatter(packages, x='Lines', y='Characters')
fig.show()
fig.write_image('scatter-lines-characters.svg')
```

[% figure
   slug="scatter-lines-characters"
   img="scatter-lines-characters.svg"
   caption="Characters vs. Lines"
   alt="Scatter plot with most values clustered in the range X equals 0 to 5,000 and Y equals 0 to 0.2 million, with some outliers."
%]

## Calculations with Dataframes

-   Best way to explore Pandas is by example
-   Since we don't know what answers to expect from calculations using the package data,
    construct a small example that we can check while we explore

```{.python title="aggregation.py"}
example = pd.DataFrame(
    data=[[  1,   2,   3],
          [ 10,  20,  30],
          [100, 200, 300]],
    columns=['left', 'middle', 'right']
)
print(example)
```
```txt
   left  middle  right
0     1       2      3
1    10      20     30
2   100     200    300
```

-   Break this down:
    -   `pd` is the alias for Pandas
    -   `DataFrame` is the kind of object we want to create
    -   `data` is a list-of-lists with the values we want in our dataframe
    -   `columns` is the names we want to give the columns
    -   We could provide `data` and `columns` in the opposite order
        and everything would still work
        because we're naming them explicitly
    -   Result is three columns and three rows
-   We can do arithmetic on entire columns

```{.python title="aggregation.py"}
print(example['middle'] + example['right'])
```
```txt
0      5
1     50
2    500
dtype: int64
```

-   If we use a plain old number it is automatically [% g broadcast "broadcast" %] to the size of the column

```{.python title="aggregation.py"}
print(7 * example['left'])
```
```txt
0      7
1     70
2    700
Name: left, dtype: int64
```

-   Sums, averages, and other functions that turn many values into one are called [% g aggregation "aggregations" %]
    -   `count`: number of elements (excluding [% g nan "`NaN`" %])
    -   `describe`: descriptive statistics
    -   `first`: first value
    -   `last`: last value
    -   `max`: largest value
    -   `mean`: average value
    -   `min`: least value
    -   `nth` : \\( n^{th} \\) value
    -   `sem`: standard error of the mean
    -   `size`: group size (including `NaN`)
    -   `std`: standard deviation
    -   `sum`: sum of values
    -   `var`: variance

<div class="callout" markdown="1">
### Not a Number, Not Available, Null, and None

`NaN` stands for "Not a Number", a special value used to represent things like
0/0 <cite>Kahan1997</cite>.  Despite the similarity in their names, it is *not*
the same thing as [% g na "`NA`" %] (Not Available), which is a
placeholder for missing values.  To make things more confusing, [% g sql "SQL" %] (the standard language for querying [% g relational_database "relational databases" %]) uses [% g null "`null`" %] instead of `NA` to signal missing data, while many
programming languages use `null` to mean "a reference that doesn't refer to
anything".  Python uses `None` instead of `null`, but we must be careful when
reading and writing data to distinguish between empty strings, missing values,
and the country code for Namibia.
</div>

-   Use the method `agg` to calculate aggregates
    -   Give it the name of a function as a string

```{.python title="aggregation.py"}
print(example.agg('sum'))
```
```txt
left      111
middle    222
right     333
dtype: int64
```

-   The sum of column `left` is 111, of column `middle` is 222, and of `right` is 333
    -   Once again `dtype` is the data type
-   We can calculate several aggregate values at once by giving `DataFrame.agg` a list of function names
    -   Exercise: is this more efficient or not?

```{.python title="aggregation.py"}
print(example.agg(['sum', 'mean']))
```
```txt
       left  middle  right
sum   111.0   222.0  333.0
mean   37.0    74.0  111.0
```

## Selecting Subsets of Data

-   Suppose we want to look at the low values in the data
-   Do this by [% g filter "filtering" %] data and calculating values for the rows we have kept
    -   "Keep" would have been a better name than "filter", but we're stuck with it
-   Create another small dataframe to demonstrate

```{.python title="filter.py"}
colors = pd.DataFrame(
    columns=['name', 'red', 'green', 'blue'],
    data=[
        ['yellow',  1.0, 1.0, 0.0],
        ['aqua',    0.0, 1.0, 1.0],
        ['fuchsia', 1.0, 0.0, 1.0]
    ]
)
print(colors)
```
```txt
      name  red  green  blue
0   yellow  1.0    1.0   0.0
1     aqua  0.0    1.0   1.0
2  fuchsia  1.0    0.0   1.0
```

-   We know how to select the `red` column

```{.python title="filter.py"}
red = colors['red']
print(red)
```
```txt
0    1.0
1    0.0
2    1.0
Name: red, dtype: float64
```

-   Now let's see where values are 1.0 and where they aren't

```{.python title="filter.py"}
has_red = (red == 1.0)
print(has_red)
```
```txt
0     True
1    False
2     True
Name: red, dtype: bool
```

-   The expression `(red == 1.0)` is no different from `(red + 3)`,
    except the result is [% g boolean "Boolean" %] instead of numeric
-   If we use a Boolean vector as an index,
    the result is a smaller table containing only the rows where the index was `True`

```{.python title="filter.py"}
rows_with_red = colors[has_red]
print(rows_with_red)
```
```txt
      name  red  green  blue
0   yellow  1.0    1.0   0.0
2  fuchsia  1.0    0.0   1.0
```

-   So we can calculate the average red, green, and blue for all colors for the whole table:

```{.python title="filter.py"}
print(colors.agg('mean'))
```
```txt
FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated;
in a future version this will raise TypeError.
Select only valid columns before calling the reduction.
red      0.666667
green    0.666667
blue     0.666667
dtype: float64
```

-   Error message is because we're trying to calculate the mean of three color names
-   We could select all the color value columns...
-   ...or select everything except `name`:
    -   Need `axis=1` to specify that we're dropping vertically rather than horizontally

```{.python title="filter.py"}
print(colors.drop('name', axis=1).agg('mean'))
```
```txt
red      0.666667
green    0.666667
blue     0.666667
dtype: float64
```

-   So let's average the color values in colors that contain some red:

```{.python title="filter.py"}
print(colors.drop('name', axis=1)[colors['red'] == 1.0].agg('mean'))
```
```txt
red      1.0
green    0.5
blue     0.5
dtype: float64
```

-   This style of programming is called [% g method_chaining "method chaining" %]
    -   Each operation like `loc` and `agg` creates a new object
    -   We immediately call a method of that new object
    -   Then call a method of the object that method returns, and so on
-   Behind the scenes, Pandas re-uses most of the data rather than copying it to make things faster

## Lines and Characters in Python Files

-   Created a scatter plot earlier
-   Construct a [% g histogram "histogram" %] to see how many [% g outlier "outliers" %] there are
    -   Add width and height for the print version

```{.python title="ratio.py"}
import pandas as pd
import plotly.express as px

packages = pd.read_csv('python-local-package-size.csv')
packages = packages[packages['Lines'] > 0]
packages['ratio'] = packages['Characters'] / packages['Lines']

fig = px.histogram(packages, x='ratio')
fig.show()
fig.write_image('hist-ratio-unscaled.svg', width=600, height=400)
```

[% figure slug="hist-ratio-unscaled"
   img="hist-ratio-unscaled.svg"
   alt="Ratio of Characters to Lines (Unscaled)"
   caption="Linear-linear histogram with a single sharp spike at X equals 0 going up to Y equals 2,200 and nothing else visible up to X equals 9,000."
%]

-   That's not very informative
    -   A few large values near x=0
    -   But a few very small values that go up over x=8000
-   Plot the logarithm of the ratio to show things more clearly <span f="hist-ratio-scaled"/>

```{.python title="ratio.py"}
fig = px.histogram(packages, x='ratio', nbins=100, log_y=True)
fig.show()
fig.write_image('hist-ratio-scaled.svg')
```

[% figure slug="hist-ratio-scaled"
   img="hist-ratio-scaled.svg"
   alt="Ratio of Characters to Lines (Scaled)"
   caption="Log-linear histogram with a single sharp spike at X equals 0 going up to Y equals 3,000 and a sharp decline to Y equals 2 near X equals 1,800 and one outlier of Y equals 2 at X equals 9,000."
%]

-   Play with a threshold for a bit and discover that less than 0.3% of records are above 100 characters per line
-   Plot all the values except these *without* logarithmic scaling
    -   Report how many were excluded so that readers know they're not seeing all the data

```{.python title="ratio.py"}
print(f"Excluding {len(packages[packages['ratio'] > 100])}/{len(packages)} data points")
fig = px.histogram(packages[packages['ratio'] <= 100], x='ratio', nbins=100)
fig.show()
fig.write_image('hist-ratio-most.svg')
```
```txt
Excluding 92 data points
```

[% figure slug="hist-ratio-most"
   img="hist-ratio-most.svg"
   alt="Ratio of Characters to Lines (Most)"
   caption="Linear-linear histogram with apparently normal distribution peaking at Y equals 2200 near X equals 35."
%]

-   Data is easier to see
-   But what (if anything) does it *mean*?
-   For that, we need some statistics

## Exercises

### Dissecting the `find` Command

Use [explainshell][explain-shell] to dissect the `find` command used to get Python file sizes.
Why is the semi-colon needed, and why does it have to have a backslash in front of it?

### One-Sided Average

Is "average" a meaningful statistic for a [% g one_sided_distribution "one-sided distribution" %]
with a [% g long_tail "long tail" %]?
What would be a better way to characterize this distribution?

### Finding Python Files

Write a short Python script to find Python source files and get their size.
(Hint: use the [`glob`][glob] module to find files.)

### Empty Python Files

Why do empty Python files exist?
Why do some files have such very long lines?
Do any files have some characters but zero lines?
How should we represent these in our visualization?

### Meaningful Axis Labels

Add meaningful axis labels to all of the plots.

### Characters Per Line

What does the distribution of characters per line tell you about these files?
How does the ratio for your own files compare?

### Resetting a Dataframe's Index

What does resetting the index of a dataframe do?
Why do we have to reset the index
in the script that counts the frequency of '.'-separated components of names?
