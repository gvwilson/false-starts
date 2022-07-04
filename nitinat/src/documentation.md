---
title: Documenting Code
---

-   Documenting little scripts written for personal use isn't worthwhile
-   But those scripts grow and are used by other people
    -   Including your future self
-   We've been writing minimal docstrings
-   [pdoc3][pdoc3] is the simplest documentation available
    -   Less effort to set up than [Sphinx][sphinx]
    -   Less frustrating than [MkDocs][mkdocs]
-   `pip install pdoc3` gives us a command `pdoc`
-   Run `pdoc --html --output-dir docs nitinat` from the command line
    -   Creates `docs/nitinat/index.html` and other files
-   Add it to `tasks.py`
    -   In the same task that builds the website
    -   After Ivy runs

```python
@task
def website(c):
    """Build website."""
    c.run("ivy build")
    c.run(f"pdoc --force --html --output-dir docs nitinat")
```

-   But wait: what if we change the Ivy configuration to put documentation somewhere else?
-   Python programs can import files in the same directory

```python
@task
def website(c):
    """Build website."""
    from config import out_dir
    c.run("ivy build")
    c.run(f"pdoc --force --html --output-dir {out_dir} nitinat")
```

-   Is this a good idea?
    -   Pro: every decision in a program should be made exactly once
    -   Con: will the next reader understand where configuration is coming from?
-   We use [Google-style docstrings][google-docstrings]

```python
def pre_stage(overall, stage):
    """Prepare for running a stage.

    Args:
        overall (dict): overall configuration.
        stage (dict): configuration for this stage.

    Returns:
        - str: function name
        - dict: function parameters
    """
    func_name = stage["function"]
    params = overall | stage
    del params["function"]
    return func_name, params
```

<div class="callout">
<dl>
<dt><code>def pre_stage(overall, stage)</code></dt>
<dd>
<div class="desc"><p>Prepare for running a stage.</p>
<p><strong>Args</strong></p>
<dl>
<dt><strong><code>overall</code></strong> : <code>dict</code></dt>
<dd>overall configuration.</dd>
<dt><strong><code>stage</code></strong> : <code>dict</code></dt>
<dd>configuration for this stage.</dd>
</dl>
<p><strong>Returns</strong></p>
<ul>
<li><code>str</code>: function name</li>
<li><code>dict</code>: function parameters</li>
</ul>
</div>
</dl>
</div>

-   Can also include examples, describe the exceptions that are raised, link to other pages, etc.
-   The more users you have, the higher the proportion of project effort goes into documentation
    -   If you'd like to be rich, famous, and popular, figure out a way to regression test docs
