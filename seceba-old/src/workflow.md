---
title: "Reproducible Workflows"
lede: "How to make sure the next person can get the same answer"
template: page
---

It's easy to run one program to process a single data file,
but what happens when our analysis depends on many files,
or when we need to re-do the analysis every time new data arrives?
What should we do if the analysis has several steps
that we have to do in a particular order?

If we try to keep track of this ourselves,
we will inevitably forget some crucial steps,
and it will be hard for other people to pick up our work.
Instead,
we should use a <span g="build_tool">build tool</span>
to keep track of what depends on what
and run our analysis programs automatically.
These tools were invented to help programmers rebuild complex software,
but can be used to automate any workflow.

<div class="callout" markdown="1">
### Make

The first widely-used build tool, Make, written in 1976.  Programmers have
created many replacements for it in the decades since then—so many, in fact,
that none have attracted enough users to displace it entirely.
</div>

When Snakemake runs,
it reads <span g="build_rule">build rules</span> from a file called `Snakefile`.
(It can be called other things, but that's the convention.)
Each rule explains how to update a <span g="build_target">target</span>
if it is out of date compared to any of its <span g="build_prerequisite">prerequisites</span>.
Here's a rule to regenerate a compressed data file `data/all-versions.csv.gz`
if the file is older than the script used to create it:

```python
rule all_versions:
    '''Download all version info from PyPI - takes several hours.'''
    output:
        protected('data/all-versions.csv.gz')
    shell:
        '''
        python bin/get-all-versions.py > data/all-versions.csv
        gzip data/all-versions.csv
        '''
```

-   First line gives the rule a meaningful name
-   Second is a docstring
    -   `snakemake --list` will show the rules and their docstrings
-   `output` section tells Snakemake what file(s) this rule produces
    -   The `protected` function tells Snakemake to change permissions on the file so it won't accidentally be deleted
    -   Only do this for files that take a long time to re-create
-   `shell` section tells Snakemake what command(s) to run to create the output
    -   It will automatically create the `data` directory if need be
    -   We can put Python directly in the Snakefile, but I prefer scripts so that commands can be re-run independently

<div class="callout" markdown="1">
### Compressing Data

Compressing this dataset takes file from 103.8 Mbyte to 9.5 Mbyte, which is
almost a factor of 11.  However, version control can only diff and merge plain
text files, so if the file is compressed, Git can't help us track changes to
individual lines.  On the other hand we probably shouldn't be changing a dataset
anyway...
</div>

-   Execute these commands with

```sh
snakemake -j 1 all_versions
```

Since that will take several hours to complete,
let's add another rule to the same file:

```python
rule releases_per_package:
    '''How many releases are there for each package?'''
    input:
        'data/all-versions.csv.gz'
    output:
        'results/releases.csv'
    shell:
        'python bin/count-releases.py {input} > {output}'
```

-   `-j1` means "only run one job at a time"
    -   Snakemake can run many jobs in parallel
-   `results/releases.csv` depends on an input data file
-   Snakemake only runs the commands if the output doesn't exist or is older than the input

`count-releases.py` is only a few lines long.
It takes advantage of the fact that if we give Pandas' `read_csv` function
a string instead of a stream
it assumes that parameter is a filename,
and that it can read directly from compressed files
(which it identifies by looking for common endings like `.zip` or `.gz`).

```py
#!/usr/bin/env python

'''
Count how many releases there are per package.
'''

import sys
import pandas as pd

def main():
    '''
    Main driver.
    '''
    data = pd.read_csv(sys.argv[1])
    result = data.groupby('Package').Release.nunique()
    result.to_csv(sys.stdout, header=True)


if __name__ == '__main__':
    main()
```
{: title="bin/count-releases.py"}

If we run:

```sh
snakemake -j1 releases_per_package
```

and wait a few seconds,
we have a file with the following:

```txt
Package,Release
0,1
0-0-1,1
0-core-client,9
0-orchestrator,14
00print-lol,2
01d61084-d29e-11e9-96d1-7c5cf84ffe8e,2
021,1
...
```

Creating a Snakefile may seem like extra work,
but few things in life are as satisfying as running one command
and watching an entire multi-step analysis run itself:

1.  It reduces errors,
    since we only have to type commands correctly once
    instead of over and over again.

2.  More importantly,
    it documents our workflow
    so that someone else (including our future self)
    can see exactly what steps we used in what order.

## How can we remove redundant releases?

-   How many packages are released in redundant formats (e.g., as both `.tar.gz` and `.whl`)?
-   First step is to find out what formats are represented in the data
    -   Break names on `.`
    -   Count how often each type of field appears

```py
#!/usr/bin/env python

import sys
import pandas as pd
from collections import Counter

def main():
    '''
    Count frequency of '.'-separated components of names.
    '''
    data = pd.read_csv(sys.argv[1])
    data = data['Release'].str.split('.', expand=True)
    data = data.values.flatten()
    data = Counter(data)
    del data[None]
    data = pd.DataFrame.from_dict(data, orient='index').reset_index()
    data = data.rename(columns={'index': 'Component', 0: 'Count'})
    data = data[~ data['Component'].str.match(r'^\d+$', na=False)]
    data = data.sort_values(by='Count', ascending=False)
    data.to_csv(sys.stdout, header=True, index=False)


if __name__ == '__main__':
    main()
```
{: title="bin/components.py"}

-   In order:
    -   Read the file
    -   Split the `Release` column on `.`, creating new columns for the fragments
    -   Flatten all those columns into a single vector
    -   Count how often each component appears
    -   Remove the `None` value (because splitting on `.` created a lot of blanks)
    -   Turn the result back into a dataframe and reset the index
        -   We explore why we need to reset the index in the exercises
    -   Give the columns sensible names
    -   Keep values that aren't composed entirely of digits (after inspection)
    -   Sort by count
    -   Save

-   We did *not* write this all at once
    -   Write the first couple of steps
    -   `gunzip -c data/all-versions.csv | head -n 10 > /tmp/test-data.csv.gz` to create a test dataset
    -   Keep adding steps
    -   Enlarge the test set once the pipeline seems to be working

-   Add a rule to `Snakefile`

```make
rule count_name_components:
    '''How often does each component of a dotted name occur?'''
    input:
        'data/all-versions.csv.gz'
    output:
        'results/name-component-count.csv'
    shell:
        'python bin/components.py {input} > {output}'
```

-   Run

```txt
Component,Count
tar,1298365
gz,1294773
whl,833181
py3-none-any,219230
egg,83174
zip,79232
0-py2,56429
0-py3-none-any,53955
1-py3-none-any,46384
1-py2,42507
2-py3-none-any,29974
2-py2,27282
3-py3-none-any,21383
3-py2,19175
exe,17161
0-py2-none-any,16079
4-py3-none-any,15782
4-py2,14105
5-py3-none-any,12791
1-py2-none-any,11683
5-py2,11233
...
```

-   Most common suffixes are `.tar.gz`, `.tar`, `.whl`, `.egg`, `.zip`, and `.exe`
    -   Need domain knowledge to recognize these
    -   And to know that `.tar` and `.gz` appear together

-   Add this rule at the top of the file
    -   Depends on two files but doesn't have an action
    -   Snakemake re-creates both files

```python
rule all:
    '''Dummy rule to rebuild everything.'''
    input:
        ['results/releases.csv', 'results/name-component-count.csv']
```

-   Next, calculate how many releases there are per package once we remove duplicates

```py
def main():
    '''
    Count releases before and after de-duplication.
    '''
    data = pd.read_csv(sys.argv[1])
    num_packages = len(data)
    data = data.assign(Stripped=data['Release'].str.replace(r'\.(tar\.gz|tar|whl|egg|zip|exe)$', ''))
    result = pd.DataFrame({'Complete': data.groupby('Package').Release.nunique(),
                           'Stripped': data.groupby('Package').Stripped.nunique()})
    num_shorter = len(result[result.Complete > result.Stripped])
    print(f'{num_shorter} / {num_packages} ({(100 * num_shorter / num_packages):6.2}%) shorter')
```
{: title="bin/remove-duplicates.py"}

-   Rule in Snakefile doesn't produce an output file
    -   Just shows us

```python
rule count_redundant_releases:
    '''How many duplicated (redundant) releases are there?'''
    input:
        'data/all-versions.csv.gz'
    shell:
        'python bin/remove-duplicates.py data/all-versions.csv.gz'
```

-   Output

```txt
2255 / 2312545 ( 0.098%) shorter
```

-   So this *isn't* a big enough issue to explain the even-numbered jagginess of our earlier figure

## Exercises

### Compressing Results

We decided to compress the source data file used in this chapter.
Should we compress the results file(s) we generate as well?
Why or why not?
