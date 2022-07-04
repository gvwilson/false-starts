---
title: Producing Results
---

-   Results go in a `results` directory
    -   Or one directory per report/paper, depending on the nature of the project
-   Add this to `tasks.py`:

```python
from pathlib import Path
from nitinat import plotting

RESULTS_DIR = "results"
PLOTS = {
    "count_by_province": plotting.histogram_by_province
}
PLOT_TYPE = ".svg"

@task
def plot_data(c):
    """Create plots of data."""
    for (stem, plot_func) in PLOTS.items():
        result = Path(RESULTS_DIR, stem).with_suffix(PLOT_TYPE)
        plot_func(CLEAN_FILE, str(result))
```

-   Python 3 has a `Path` module for creating and manipulating file paths
-   Going to create another file in the module called `plotting`
    -   Specify the plots we want with a dictionary mapping plot names to the functions that create those plots
    -   Specify the plot type separately so we can change our minds later
    -   Inside the task, call each plotting function with the data and the name of the output file
-   Start with a single plotting function:

```python
"""Create plots."""

import plotly.express as px


from .data import read_clean_data


def histogram_by_province(datafile, plotfile):
    """Create histogram of measurements by province."""
    df = read_clean_data(datafile)
    fig = px.histogram(df, x="province",
                       category_orders={"province": df["province"].cat.categories})
    fig.write_image(plotfile)
```

-   Run with `inv plot-data`

![Reports by province](@root/count_by_province.svg)
