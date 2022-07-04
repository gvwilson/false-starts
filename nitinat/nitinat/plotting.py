"""Create plots."""

from datetime import datetime

import plotly.express as px

from .data import read_clean_data


def count_by_analyte(datafile, plotfile):
    """Create histogram of measurements by analyte."""
    df = read_clean_data(datafile)
    fig = px.histogram(df, x="analyte")
    fig.write_image(plotfile)


def count_by_province(datafile, plotfile):
    """Create histogram of measurements by province."""
    df = read_clean_data(datafile)
    category_orders = {"province": df["province"].cat.categories}
    fig = px.histogram(df, x="province", category_orders=category_orders)
    fig.write_image(plotfile)


def sample_vs_analysis_date(datafile, plotfile):
    """Create scatter plot of sample and analysis dates."""
    df = read_clean_data(datafile)
    for colname in ("sample_date", "analysis_date"):
        df[colname] = df[colname].map(datetime.toordinal)
    fig = px.scatter(df, x="sample_date", y="analysis_date", trendline="ols")
    tick_x = df["sample_date"].map(
        lambda x: datetime.fromordinal(x).strftime("%b %d")
    )
    fig.update_xaxes(tickvals=df["sample_date"], ticktext=tick_x)
    tick_y = df["analysis_date"].map(
        lambda x: datetime.fromordinal(x).strftime("%b %d")
    )
    fig.update_yaxes(tickvals=df["analysis_date"], ticktext=tick_y)
    fig.write_image(plotfile)
