"""Handle details of particular datasets."""

import pandas as pd

from . import get_logger

EXCEL_ENCODING = "Windows-1252"
COLUMNS = {
    "Food Name": "food_name",
    "Sample Collection Date": "sample_date",
    "Human Illness Flag": "illness",
    "Sampling Location Province": "province",
    "Analysis Completion Date": "analysis_date",
    "Result Value": "reading",
    "Units of measurement": "units",
    "Analyte Name": "analyte",
}
PROVINCES = (
    ("British Columbia", "BC"),
    ("Alberta", "AB"),
    ("Saskatchewan", "SK"),
    ("Manitoba", "MB"),
    ("Ontario", "ON"),
    ("Quebec", "QC"),
    ("New Brunswick", "NB"),
    ("Nova Scotia", "NS"),
    ("Prince Edward Island", "PE"),
    ("Newfoundland and Labrador", "NL"),
)


def clean_raw_data(filename):
    """Extract subset of interest from raw data."""
    logger = get_logger()
    df = pd.read_csv(filename, encoding=EXCEL_ENCODING)
    df = df[[col for col in COLUMNS.keys()]]
    df.rename(columns=COLUMNS, inplace=True)
    logger.info(
        f"clean {filename}: {len(df.columns)} columns x {len(df.index)} rows"
    )
    return df


def read_clean_data(filename):
    """Read cleaned-up data."""
    logger = get_logger()
    df = pd.read_csv(filename)
    province_cat = [p[0] for p in PROVINCES]
    df["province"] = pd.Categorical(
        df["province"], province_cat, ordered=True
    ).rename_categories({p[0]: p[1] for p in PROVINCES})
    for colname in ("sample_date", "analysis_date"):
        df[colname] = pd.to_datetime(df[colname])
    logger.info(
        f"read {filename}: {len(df.columns)} columns x {len(df.index)} rows"
    )
    return df
