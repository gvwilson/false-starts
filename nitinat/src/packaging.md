---
title: Creating a Package
---

-   Programming mostly consists of gluing libraries together to build more libraries
    -   "Create a little language in which the solution to your problem is straightforward"
-   Python's packages are one of its greatest strengths, but Python's packaging tools are one of its greatest weaknesses
    -   Things are getting better, but we're not there yet
-   The first step is to decide what kind of package and what tools to use
    -   [conda][conda] is the "right" answer, but complex to set up (even with copy and paste)
    -   New tools like [poetry][poetry] and [flit][flit] are the future
    -   We're going to stick to [pip][pip] because at least its headaches are well understood
-   Add a few lines to `pyproject.toml` to tell it what build system we're using

```
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 80

[tool.flake8]
max-line-length = 80

[tool.isort]
profile = "black"
```

-   Re-create the `setup.cfg` file we [got rid of](@root/technical-debt-02//)
    -   To create a package, Python eventually calls `setuptools.setup`
    -   We can do this directly in a file that's typically called `setup.py`
    -   Or put parameter values for that function call in `setup.cfg`

```
[metadata]
name = nitinat
version = attr: nitinat.__version__
author = Greg Wilson
author_email = greg@deepgenomics.com
description = A model data analysis project
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/gvwilson/nitinat
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
packages = nitinat
python_requires = >=3.9
install_requires =
  kaleido >= 0.2
  pandas >= 1.4
  plotly >= 5.6
  pydantic >= 1.9.0
  pyyaml >= 5.4
  requests >= 2.27
  statsmodels >= 0.13
```

-   The `[metadata]` section describes our package
    -   `attr: nitinat.__version__` means "load the `nitinat` package and use its `__version__` (to avoid duplicating information)
    -   `file: README.md` means "read this file and use its content verbatim"
    -   The `classifiers` are used to categorize the package on [PyPI][pypi]: please look there for other relevant values
-   The `[options]` section is what we want to build
    -   `install_requires` defines the dependencies that are needed for installation, not for development

<div class="callout" markdown="1">
### `setup.cfg` vs. `requirements.txt`

The information in `[install_requires]` is a subset of what's in `requirements.txt`.
There are ways to avoid this duplication,
but they're all brittle and we hope the need for them will go away within a year.
For now, duplicating is easier than debugging.
</div>

-   Install the package in "edit mode" in the current conda environment:

```shell
$ pip install -e .
Obtaining file:///u/nitinat
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: requests>=2.27 \
  in /u/conda/envs/nitinat/lib/python3.9/site-packages (from nitinat==0.1.0) (2.27.1)
Requirement already satisfied: pyyaml>=5.4 \
  in /u/conda/envs/nitinat/lib/python3.9/site-packages (from nitinat==0.1.0) (5.4.1)
...more like this...
Installing collected packages: nitinat
  Running setup.py develop for nitinat
Successfully installed nitinat-0.1.0
```

-   Did that work?
    -   We now have a directory `./nitinat.egg-info/` with leftovers from the build
-   Go into another directory (so that `import` doesn't pick up the sub-directory) and import it

```shell
$ cd /tmp
$ python
Python 3.9.12 | packaged by conda-forge | (main, Mar 24 2022, 23:27:05) 
[Clang 12.0.1 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import nitinat
>>> nitinat.__version__
'0.1.0'
>>> nitinat.__path__
['/u/nitinat/nitinat']
```

-   Can build this and upload it to PyPI using [twine][twine]
    -   Yes, another tool...
-   Or install directly from GitHub:

```shell
$ pip install git+ssh://git@github.com/gvwilson/nitinat
```

-   This installs into the current environment just like any other package
-   But the package isn't as findable and can't (easily) be listed as a dependency by other packages

<div class="callout" markdown="1">
### Oops

Did `git add` and `git commit`, then pulled changes on another machine,
but `site/project.md` wasn't there.
Turns out that the default `.gitignore` file for Python projects ignores `site/`
because that's the output directory for [MkDocs][mkdocs].
Renamed `site` back to `src`.
</div>
