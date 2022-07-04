---
title: Pipeline Revisited
---

-   We want global configuration (passed to all stages) as well as local (per-stage)
    -   I.e., a configuration file like this:

```yaml
- overall:
    debug: true
- function: reader
- function: head
  num: 1000
```

-   Would also prefer not to have to pass in all the needed functions separately
-   And requiring `reader` to take `None` as the first parameter seems clumsy
    -   Listen to our code
-   [Test-driven development][tdd] (TDD) doesn't actually improve productivity ([evidence][tdd-nwit])
    -   But working backwards from a test you have can be a good way to *explain* a design
-   Eventually wrote this:

```python
def test_pipeline2_two_stage_with_yaml_text(available):
    config = dedent("""\
    - overall:
        debug: true
    - function: reader
    - function: head
      num: 1000
    """)
    config = yaml.safe_load(config)
    with patch(READ_CONFIG, return_value=config):
        result = pipeline("test.yml", available)
        assert len(result) == 1
```

-   The `available` fixture is a dictionary of functions the pipeline can use
    -   `textwrap.dedent` moves text back to the left margin
        -   So this is what our YAML configuration file would look like
    -   The new `pipeline` function always starts with a reader
        -   That's probably too far the other way
    -   The global `debug` flag overrides the `num` setting in `head`:

```python
def head(df, num, debug=False):
    """To demonstrate pipeline operation."""
    return df.head(1) if debug else df.head(num)
```

-   `debug` has a default value so we don't have to provide it every time
-   The revised `pipeline` function is:

```python
def pipeline(config_file, available):
    """Construct and run a processing pipeline."""
    # Set up.
    raw_config = _read_config(config_file)
    overall, stages = split_config(raw_config)

    # Run each stage in turn.
    data = None
    for stage in stages:
        func = get_function(available, stage["function"])
        params = overall | {k: stage[k] for k in stage if k != "function"}
        data = func(**params) if (data is None) else func(data, **params)

    # Return final result.
    return data
```

-   Read the configuration file
    -   Again, keep this in a separate function for easy mocking
-   Split the configuration into overall and per-stage
-   Initially have no data
-   For each stage:
    -   Get the function
    -   Construct parameters: per-stage overrides overall
    -   Call the function with data if we have any or with nothing if we don't
-   Splitting the configuration is straightforward:

```python
def split_config(raw):
    """Split configuration into overall and per-stage."""
    for (i, entry) in enumerate(raw):
        if "overall" in entry:
            del raw[i]
            return entry["overall"], raw
    return {}, raw
```

-   OK, I lied: it took a couple of tries to come up with this
    -   The overall configuration is a dictionary with one key ("overall")
-   Getting the function is straightforward:

```python
def get_function(available, name):
    """Look up a function by name."""
    assert name in available
    return available[name]
```

-   Could move this inline
    -   But it's likely to become more complicated...
    -   ...and we're going to want to add better error handling than a simple `assert`
    -   Experience (i.e., past difficulties) tell us when to plan and design ahead
-   Lots here to test, but one key feature is that we can debug individual stages:

```python
READER_SHORTENED_LEN = 3

def reader(debug=False):
    """To demonstrate pipeline operation."""
    df = simple_df()
    return df.head(READER_SHORTENED_LEN) if debug else df

def test_pipeline2_single_stage_with_debugging(available):
    config = [{"function": "reader", "debug": True}]
    with patch(READ_CONFIG, return_value=config):
        result = pipeline("test.yml", available)
        assert len(result) == READER_SHORTENED_LEN
```

-   Test code should be written as cleanly as production code
    -   Which is why this code now has `READER_SHORTENED_LEN`
    -   Because an earlier version of the just used the number 3...
    -   ...which stopped working when we changed it in one place but not another
-   One final step: `inv coverage`
    -   Tells us that `_read_config` isn't being tested
    -   Could add a test that reads from an actual file...
    -   ...or add a directive in a specially-formatted comment telling coverage not to worry about it

```python
def _read_config(filename):  # pragma: no cover
    """Read YAML configuration file."""
    with open(filename, "r") as reader:
        return yaml.safe_load(reader)
```

-   Please use these sparingly
