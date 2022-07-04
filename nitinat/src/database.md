---
title: Accessing a Database
---

-   Sooner or later every project needs to get data from a database
    -   A relational database like [PostgreSQL][postgresql] or [SQLite][sqlite]
    -   As opposed to a document database like [MongoDB][mongo] or [Firestore][firestore]
-   Write queries for relational databases using [SQL][sql] (pronounced in a variety of ways)
    -   For an introduction, see [the Carpentries lesson][carpentries-sql]
-   One way to get data into a program is to use a Unix command-line pipe

```shell
$ sqlite3 mydata.db myquery.sql | python myscript.py
```

-   This becomes very clumsy very quickly
-   Another approachis to embed SQL commands as text in the Python program:

```python
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
```
```
('2013-09-15', '2014-05-15', 'Potassium-40', 660.7555)
('2015-01-15', '2015-06-15', 'Potassium-40', 641.0498)
('2020-11-01', '2021-08-23', 'Potassium-40', 633.3652)
('2019-10-25', '2020-03-23', 'Potassium-40', 619.2273)
('2019-10-25', '2020-03-23', 'Potassium-40', 611.1997)
```

-   A third approach is to use an [object-relational mapper][orm]
    -   Translates objects into queries and query results back into objects
-   Most popular for Python is [SQLAlchemy][sqlalchemy], which does a lot but is complex
-   [Ibis][ibis] isn't as mature, but also isn't as large
-   `pip install sqlalchemy ibis-framework`
    -   Ibis uses SQLAlchemy under the hood
-   Query result is a [Pandas][pandas] dataframe, which is nice

```python
connection = ibis.sqlite.connect(db_file_name)
samples = connection.table("Samples")
query = samples["sample_date", "analysis_date", "analyte", "reading"]\
    .filter((samples.analyte == "Potassium-40") & (samples.reading > 0))\
    .sort_by(ibis.desc("reading"))\
    .limit(5)
print(query.execute())
```
```
  sample_date analysis_date       analyte   reading
0  2013-09-15    2014-05-15  Potassium-40  660.7555
1  2015-01-15    2015-06-15  Potassium-40  641.0498
2  2020-11-01    2021-08-23  Potassium-40  633.3652
3  2019-10-25    2020-03-23  Potassium-40  619.2273
4  2019-10-25    2020-03-23  Potassium-40  611.1997
```

-   In most cases, the only thing that changes when switching to different database server is creating the connection

```python
connection = ibis.postgresql.connect("user:password@localhost:5432/dbname")
```

-   All of the queries stay the same...
-   ...until you use something that is database-specific, because every DB has its own dialect of SQL
    -   That's a problem with the embedded SQL approach as well
-   But now it all goes sideways
-   `inv website` fails with `AttributeError: module 'ibis' has no attribute 'loaders'`
-   Because [Ivy][ivy] depends on an HTML template module called (wait for it) Ibis
-   The `ibis-framework` package creates something we need to import with `import ibis`
-   *This isn't supposed to happen* (and bug reports have been filed)

<div class="callout" markdown="1">
### Where These Examples Are

The code that creates the database and does queries with embedded SQL and Ibis
lives in `bin/sql-example.py` rather than in the `nitinat` package.
</div>
