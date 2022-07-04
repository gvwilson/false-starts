---
title: Improving the Website
---

-   [Ivy][ivy]'s `graphite` theme isn't an efficient use of space for what we want to show
-   So create one of our own
-   `lib/genomic/templates/node.ibis` lays out the page
-   `lib/genomic/resources/theme/*.css` does the styling
    -   `genomic.css` with minimal styling of our own
    -   Copy `tango.css` from [pygments-css][pygments-css]
-   Move our links extension to `lib/genomic/extensions/links.py`
-   Set `res_dir` to `results` in `config.py`
    -   All of our results will be copied to the website for inclusion in pages
    -   Might want to re-think this if results files are large or confidential
-   Rebuild everything and commit `docs` directory
-   Is it worth doing?
    -   Maybe not yet, but wait until we start generating pages for results
    -   And documenting code
