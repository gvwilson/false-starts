---
title: Technical Debt
---

-   Time to fix that trendline bug
-   Step 1: re-create the conda environment with Python 3.9 instead of 3.10 to avoid problems with `statsmodels`
    -   At the time of writing `pip install statsmodels` works with 3.9 but not with 3.10
    -   Add to `requirements.txt`
-   Step 2: ask a colleague for help
    -   Least squares can't calculate the square of a datetime
    -   So add some conversion to the plotting function's just-loaded copy of the dataframe

```python
def sample_vs_analysis_date(datafile, plotfile):
    """Create scatter plot of sample and analysis dates."""
    df = read_clean_data(datafile)
    for colname in ("sample_date", "analysis_date"):
        df[colname] = df[colname].map(datetime.toordinal)
    fig = px.scatter(df, x="sample_date", y="analysis_date", trendline="ols")
    tick_x = df['sample_date'].map(lambda x: datetime.fromordinal(x).strftime('%b %d'))
    fig.update_xaxes(tickvals=df['sample_date'], ticktext=tick_x)
    tick_y = df['analysis_date'].map(lambda x: datetime.fromordinal(x).strftime('%b %d'))
    fig.update_yaxes(tickvals=df['analysis_date'], ticktext=tick_y)
    fig.write_image(plotfile)
```

-   Won't affect anything else, since the dataframe is created by loading the file here
    -   *Shouldn't* affect anything else, because other code may actually want `datetime`
-   Plot now works, so commit the fix with `Closes #3` in the body of the commit message
    -   But the spacing on the axes is uneven
    -   File a bug against [Plotly][plotly] [#3641][plotly-3641]
