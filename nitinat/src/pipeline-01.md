---
title: Creating a Pipeline
---

-   Want reproducible data processing pipelines with a "test run" option
    -   Several moving parts, so do it in steps
-   We could write this:

```python
start = pd.read_csv("input.csv")
result = third(second(first(start)))
result.to_csv("output.csv")
```

-   But if we have parameters it becomes:

```python
start = pd.read_csv("input.csv")
result = third(second(first(start, alpha), beta, gamma), delta, epsilon)
result.to_csv("output.csv")
```

-   Quick, which function is getting `delta` as a parameter?
    -   And how does someone reproduce this without reading the history of your GitHub repo?
-   Break it down to more readable steps:

```python
data = pd.read_csv("input.csv")
data = first(data, alpha)
data = second(data, beta, gamma)
data = third(data, delta, epsilon)
data.to_csv("output.csv")
```

-   But a function is just another kind of object, so we can put it in a list...
-   ...and we can spread keyword arguments in a call using `*`

```python
pipeline = [
    [first, alpha],
    [second, beta, gamma],
    [third, delta, epsilon]
]
data = pd.read_csv("input.csv")
for step in pipeline:
    func, params = step[0], step[1:]
    data = func(data, *params)
data.to_csv("output.csv")
```

-   Every function remembers the name it was given when it was defined

```python
def proof(x, y):
    pass
print(proof.__name__)
#> proof
```

-   So we can convert a list of functions into a lookup table

```python
def make_table(*functions):
    return {f.__name__: f for f in functions}

def left(): pass
def right(): pass

table = make_table(left, right)
print(table)
#> {'left': <function left at 0x101a3bdc0>, 'right': <function right at 0x101a3bee0>}
```

-   Which means we should be able to run a pipeline from a YAML file that looks like this:

```yaml
- function: left
  count: 3
- function: right
  size: 0.9
```

-   Here's the code:

```python
def pipeline(config_file, data, *functions):
    """Construct and run a processing pipeline."""
    # Set up.
    config = _read_config(config_file)
    functions = {f.__name__: f for f in functions}

    # Run each stage in turn.
    for stage in config:
        func = functions[stage["function"]]
        params = {key: stage[key] for key in stage if key != "function"}
        data = func(data, **params)

    # Return final result.
    return data

def _read_config(filename):
    with open(filename, "r") as reader:
        return yaml.safe_load(reader)
```

-   Read the YAML configuration file (in a separate function so we can replace it for testing)
-   Create a lookup table from function name to function
    -   `pipeline` has been given the functions it's allowed to call
-   For each stage in the configuration file:
    -   Find the function in the lookup table
    -   Assemble the parameters in a dictionary (rather than a list) *without* the function name
    -   Call the function with the current data
    -   Return the final result

-   Here are three functions we can use to test this:

```python
def first(df):
    return df.iloc[[0]]

def head(df, num):
    return df.head(num)

def tail(df, num):
    return df.tail(num)
```

-   Yes, they're trivial, but we *want* trivial for testing
-   Let's create a simple dataframe for testing:

```python
@fixture
def simple_df():
    return pd.DataFrame({
        "red": [0.1, 0.2, 0.3],
        "green": [0.4, 0.5, 0.6],
        "blue": [0.7, 0.8, 0.9]
    })
```

-   An empty pipeline should just return the original data

```python
READ_CONFIG = "nitinat.pipeline._read_config"

def test_pipeline_empty_returns_original_data(simple_df):
    config = []
    with patch(READ_CONFIG, return_value=config):
        result = pipeline("test.yml", simple_df)
        assert result.equals(simple_df)
```

-   Here's a more complex pipeline:

```python
def test_pipeline_multiple_functions(simple_df):
    config = [
        {"function": "head", "num": 2},
        {"function": "tail", "num": 1}
    ]
    with patch(READ_CONFIG, return_value=config):
        result = pipeline("test.yml", simple_df, head, tail)
        assert len(result) == 1
        assert result.equals(simple_df.iloc[[1]])
```

-   One more test: configuration file and data file on disk

-   Add a reader function
    -   Must be the first in the pipeline, so incoming dataframe must be `None`

```python
def reader(df, filename):
    """To demonstrative pipeline operation."""
    assert df is None
    with open(filename, "r") as reader:
        return pd.read_csv(reader)
```

-   Write a configuration file

```yaml
- function: reader
  filename: three-colors.csv
- function: head
  num: 1
```

-   Create the data file

```
red,green,blue
0.1,0.4,0.7
0.2,0.5,0.8
0.3,0.6,0.9
```

-   Write the test

```python
def test_pipeline_with_real_files():
    filename = Path(__file__).parent.joinpath("simple-pipeline.yml")
    result = pipeline(filename, None, reader, head)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
```

-   Again, the special variable `__file__` holds the full path of this file
    -   Its parent is the directory that contains it
    -   So the complicated `Path` expression gets `simple-pipeline.yml` in the current directory
-   Run this: it fails

```
FileNotFoundError: [Errno 2] No such file or directory: 'three-colors.csv'
```

-   Problem is that the current working directory when we run tests is the root directory of the project
    -   And our file is in `tests/three-colors.csv`, not `./three-colors.csv`
-   Temporary solution: modify the configuration file

```yaml
- function: reader
  filename: tests/three-colors.csv
- function: head
  num: 1
```

-   Now the test runs
-   Create issue #8 as a reminder to handle paths more intuitively
    -   Will people expect the path to the data file to be relative to the config file, or to the launch directory?
