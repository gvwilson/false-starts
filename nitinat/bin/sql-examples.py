#!/usr/bin/env python

"""Create SQLite database from CSV file."""

import csv
import sqlite3
import sys

import ibis

CREATE = """\
DROP TABLE IF EXISTS Samples;
CREATE TABLE Samples(
    "food_name" TEXT,
    "sample_date" DATE,
    "illness" TEXT,
    "province" TEXT,
    "analysis_date" DATE,
    "reading" REAL,
    "units" TEXT,
    "analyte" TEXT
);
"""
INSERT = "INSERT INTO Samples VALUES(?, ?, ?, ?, ?, ?, ?, ?);"


assert len(sys.argv) == 3, f"Usage: {sys.argv[0]} db_file_name csv_file_name"
db_file_name = sys.argv[1]
csv_file_name = sys.argv[2]

# ----------------------------------------
# Create
# ----------------------------------------

conn = sqlite3.connect(db_file_name)
cur = conn.cursor()
cur.executescript(CREATE)

with open(csv_file_name, newline="") as raw:
    cooked = csv.reader(raw, dialect="unix")
    next(cooked)  # skip header line
    cur.executemany(INSERT, [r for r in cooked])

conn.commit()

# ----------------------------------------
# Select using embedded SQL
# ----------------------------------------

connection = sqlite3.connect(db_file_name)

query = """\
  SELECT sample_date, analysis_date, analyte, reading
  FROM Samples
  WHERE (analyte = "Potassium-40") and (reading > 0)
  ORDER BY reading DESC
  LIMIT 5;
"""

cursor = connection.execute(query)
for row in cursor:
    print(row)

connection.close()

# ----------------------------------------
# Select using Ibis
# ----------------------------------------

connection = ibis.sqlite.connect(db_file_name)
samples = connection.table("Samples")
query = (
    samples["sample_date", "analysis_date", "analyte", "reading"]
    .filter((samples.analyte == "Potassium-40") & (samples.reading > 0))
    .sort_by(ibis.desc("reading"))
    .limit(5)
)
print(query.execute())
