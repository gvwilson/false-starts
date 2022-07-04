---
title: Indexing Datasets
---

-   The project will contain more datasets as it grows
    -   Findability will be a challenge
    -   So start to index them now
-   *This is not research* and researchers shouldn't have to spend time doing it
    -   This is plain old text wrangling and programmers should create tools that researchers can just use
    -   Put it here for completeness
-   Options:
    1.  Generate an index page from scratch: but we have HTML generators
    2.  Extend [pdoc3][pdoc3]: but the index isn't part of the code docs
    3.  Extend [Ivy][ivy]: least painful
-   Took about an hour to figure out how to add things and another hour to debug and polish
    -   Only worth it if the code and the knowledge are going to be re-used
-   Add this to Ivy's `config.py`
    -   Where the dataset descriptions will go
    -   What filename pattern (a.k.a. "glob") matches datasets (we'll actually use parameter sets since we already have them)
    -   What page template to fill in

```python
# Dataset pattern, template, and output directory
data = {
    "out_dir": "data",
    "src_glob": "parameters/*.json",
    "template": "datapage.html",
}
```

-   The page template is:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ site.title }}: {{ title }}</title>
    <link rel="stylesheet" href="@root/theme/nitinat.css">
    <link rel="stylesheet" href="@root/theme/tango.css">
  </head>
  <body>
    <h1>{{ site.title}}: {{ title }}</h1>
    <table>
      <tr><th>Key</th><th>Value</th></tr>
      {% for key, value in data.items() %}
      <tr><td>{{ key }}</td><td>{{ value }}</td></tr>
      {% endfor %}
    </table>
  </body>
</html>
```

-   Create a file `lib/nitinat/extensions/datasets.py` to hold the extensions
-   Collect information early in Ivy's processing cycle and add it to the configuration

```python
@ivy.events.register(ivy.events.Event.INIT)
def collect():
    """Collect information about datasets."""
    if "data" not in ivy.site.config:
        return
    pattern = str(Path(ivy.site.home(), ivy.site.config["data"]["src_glob"]))
    data = []
    for filename in glob.glob(pattern):
        with open(filename, "r") as reader:
            title = Path(filename).name
            data.append({
                "title": title,
                "src": filename,
                "dst": _output_filename(title),
                "data": json.load(reader)
            })
    ivy.site.config["data"]["datasets"] = data
```

-   Write files late in the processing cycle

```python
@ivy.events.register(ivy.events.Event.EXIT)
def write():
    """Write information about datasets."""
    if "data" not in ivy.site.config:
        return

    out_dir = _output_directory()
    out_dir.mkdir(mode=0o755, parents=True, exist_ok=True)

    template_path = str(
        Path(ivy.site.theme(),
             "templates", ivy.site.config["data"]["template"])
    )
    with open(template_path, "r") as reader:
        template = ibis.Template(reader.read())

    site = {"title": ivy.site.config["title"]}
    for dataset in ivy.site.config["data"]["datasets"]:
        dst = Path(out_dir, _output_filename(dataset["title"]))
        result = template.render({"site": site} | dataset)
        result = ivy.utils.rewrite_urls(result, dst)
        with open(dst, "w") as writer:
            writer.write(result)
```

-   Generate an index of datasets

```python
@shortcodes.register("datasets")
def index(pargs, kwargs, node):
    """Generate index of datasets."""
    entries = []
    for dataset in ivy.site.config["data"]["datasets"]:
        relative = Path(ivy.site.config["data"]["out_dir"], dataset["dst"])
        entries.append(f'<li><a href="./{relative}">{dataset["title"]}</a></li>')
    return "<ul>\n" + "\n".join(entries) + "\n</ul>"
```

-   Add this page to the source pages to contain the index

```
---
title: Parameter Sets
---

[% datasets %]
```

-   Index page:

<div class="html">
<h1>Parameter Sets</h1>
<ul>
<li><a href="./data/fraction-0.1.json.html">fraction-0.1.json</a></li>
<li><a href="./data/nth-50.json.html">nth-50.json</a></li>
</ul>
</div>

-   Dataset page (again, we're using the parameter sets for examples)

<div class="html">
<h1>Nitinat: fraction-0.1.json</h1>
<table>
  <tr><th>Key</th><th>Value</th></tr>
  <tr><td>fraction</td><td>0.1</td></tr>
</table>
</div>
