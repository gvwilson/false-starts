---
title: Creating a Website
---

-   Every project should have a website
-   Build with a static site generator (of which [there are many][ssg])
-   We use [Ivy][ivy] because it's still small and fast
-   Install with `pip`
    -   Add to `requirements.txt`
-   `ivy init` in the root directory
-   Edit `config.py` (and wish we could put configuration in `pyproject.toml`)
-   Take content out of `README.md` and create files in `src/*.md`
-   Add `website` task
-   After a bit of fiddling, install `pymdown-extensions` and tweak the CSS to improve rendering of code blocks
-   One weakness: have to remember to add items to `inc/menu.md`
    -   Write a table of contents extension some day
-   Borrow an extension from another project that allows a unified table of Markdown links in `links.md`
-   And remember to add a `.nojekyll` file to stop GitHub from trying to build the website with Jekyll
    -   Commit generated HTML to `./docs` instead
