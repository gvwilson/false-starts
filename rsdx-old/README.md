# Research Software Design by Example

## Introduction
*An overview of where we're going and why.*
- Assume you know how to program.
- Want to learn how to design pieces of software that are reliable and reusable.
- Best way is through examples: principles don't make sense unless you know how to translate them into specifics.

## Parse Raw Data
*Convert some messy CSV data files with geocoded pollution measurements into tidy CSV.*
- Writing command-line tools that respect [Taschuk's Rules][taschuk].
- Creating a data manifest (and why you want one).
- Using regular expressions if you have to, but an out-of-the-box parser if one is available.

## Work with Geocoded Data
*Find the center point of each polluted region and visualize it.*
- Finding, installing, and figuring out how to use open source packages.
- Using [`geopy`][geopy] to handle geocoded data.
- Plotting (and the challenge of testing visualization code).
- Creating a data manifest (and why you want one).

## Initial Invasion Percolation Script
*Walk through a student-quality Python script that uses invasion percolation to model pollution spread.*
- Reading code.
- Breaking code into comprehensible chunks.
- Writing docstrings and generating documentation pages.

## A Grid Abstraction
*Refactor the invasion percolation script into classes with two different grid implementations.*
- Creating classes and class hierarchies.
- Deciding what goes where in such a hierarchy.
- Validating implementations against one another.

## Test Invasion Percolation
*Use mocks to test a program like invasion percolation that relies on pseudo-randomness.*
- Deciding what tests to write (assume readers have already met [`pytest`][pytest]).
- Creating and using mock objects.
- Making "random" reproducible.

## Measure Performance
*Compare the performance of two grid implementations empirically.*
- Using [`coverage`][coverage] to determine which parts of the code are(n't) being exercised by tests.
- Using [`cProfile`][profile] to determine which parts are expensive.

## A Pipeline Runner
*Convert the performance measurement scripts to use a pipeline runner.*
- Describing workflows as directed acyclic graphs.
- Expressing DAGs in code with [Metaflow][metaflow].

## A Lazy Algorithm
*Create a lazy implementation of invasion percolation that's much (much) faster.*
- Estimating algorithm performance with big-oh.
- Extending a class hierarchy to accommodate new features.
- Adapting tools written earlier to make all of this simpler to run, test, and document.

## Measure Percolate Properties
*Use remote storage for large files when measuring fractal dimension and density.*
- Saving fractals created by invasion percolation for analysis.
- Using [DVC][dvc] to store those remotely instead of committing to version control.
- Using those files to estimate fractal dimension and density vs. distance from centroid.

## Search for Mutations
*Analyze genomic data from snails in polluted areas to see if a single mutation accounts for differences in sizes.*
- Using a statistical model of single nucleotide polymorphisms (SNPs) to synthesize test data.
- Building a pipeline to analyze and visualize that data.

## Interact with a Database
*Get data from a SQL database instead of from CSV files on disk.*
- Connecting to a database from Python.
- Embedding SQL queries in Python and reading results.
- Safely parameterizing SQL queries.
- Creating classes with [Pony][pony] ORM to mirror database tables.
- Writing queries in Python rather than as embedded SQL strings.

## Build a Web Service
*Build a small [Flask][flask] web server to display plate data.*
- Routing HTTP requests to functions.
- Creating HTML pages from templates.

## Conclusion
*What we've covered and where readers might like to go next.*
- Summarize key ideas.


[aosa]: https://aosabook.org/
[carpentries]: https://carpentries.org/
[coverage]: https://coverage.readthedocs.io/
[dvc]: https://dvc.org/
[contact_email]: mailto:gvwilson@third-bit.com
[flask]: https://flask.palletsprojects.com/
[geopy]: https://geopy.readthedocs.io/
[gnu_make]: https://www.gnu.org/software/make/
[gvwilson]: https://third-bit.com/
[metaflow]: https://metaflow.org/
[pony]: https://ponyorm.org/
[profile]: https://docs.python.org/3/library/profile.html
[pytest]: https://docs.pytest.org/
[sdxjs]: https://third-bit.com/sdxjs/
[sdxpy]: https://third-bit.com/sdxpy/
[t3]: https://teachtogether.tech/
[taschuk]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412
