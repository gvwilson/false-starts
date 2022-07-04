---
title: A Pipeline with Provenance
---

-   We want to know what each run of a pipeline actually did
    -   Automatically record functions and their parameters in a structured way
    -   Would also like to introduce a little error handling
-   Rewrite `pipeline` to capture functions' parameters:

```python
def pipeline(config_file, available):
    """Construct and run a processing pipeline."""
    # Set up.
    raw_config = _read_config(config_file)
    overall, stages = split_config(raw_config)

    # Run each stage in turn.
    data = None
    provenance = []
    for stage in stages:
        func_name, params = pre_stage(overall, stage)
        record, data = run_stage(available, func_name, params, data)
        provenance.append(record)
        if record["exc"] is not None:
            return provenance, None

    # Return final result.
    return provenance, data
```

-   Convert overall configuration and stage configuration into function name and parameters
    -   Run that stage, getting a record of what happened and the data to pass on
    -   Save that record
    -   If an exception occurred, stop the pipeline
    -   Only return data if the pipeline ran to the end
-   Getting the function name and parameters is just dictionary juggling:

```python
def pre_stage(overall, stage):
    """Get function, parameters, and provenance record."""
    func_name = stage["function"]
    params = overall | stage
    del params["function"]
    return func_name, params
```

-   Running the stage:

```python
def run_stage(available, func_name, params, data):
    """Run a single stage, recording provenance."""
    func = get_function(available, func_name)
    try:
        start = _now()
        data = func(**params) if (data is None) else func(data, **params)
        params["exc"] = None
    except Exception as exc:
        params["exc"] = repr(exc)
    finally:
        params["elapsed"] = (_now() - start).total_seconds()
        params["function"] = func_name
    return params, data
```

-   Steps:
    -   Look up the function
    -   Record a start time
    -   Call the function
    -   If an exception occurred, save it
    -   *Always* record the end time and the function name
-   Updating the tests

```python
def test_pipeline3_two_stages_with_parameters_no_overall(available):
    config = [{"function": "reader"}, {"function": "head", "num": 2}]
    with (
        patch(READ_CONFIG, return_value=config),
        patch(NOW, side_effect=times(2)),
    ):
        provenance, result = pipeline("test.yml", available)
        assert len(result) == 2
        assert result.equals(simple_df().iloc[[0, 1]])
        assert provenance == [
            {"exc": None, "elapsed": 1.0, "function": "reader"},
            {"exc": None, "elapsed": 1.0, "function": "head", "num": 2},
        ]
```

-   Need a helper function `times` to generate predictable times

```python
NOW = "nitinat.pipeline3._now"

def times(num_stages):
    return [datetime(2022, 1, 1, 1, 1, i) for i in range(2 * num_stages)]
```

-   Always test error handling

```python
def test_pipeline3_two_stages_with_failure(available):
    config = [{"function": "reader"}, {"function": "failure"}]
    with (
        patch(READ_CONFIG, return_value=config),
        patch(NOW, side_effect=times(2)),
    ):
        provenance, result = pipeline("test.yml", available)
        assert result is None
        assert provenance == [
            {"exc": None, "elapsed": 1.0, "function": "reader"},
            {
                "exc": "ValueError('failure message')",
                "elapsed": 1.0,
                "function": "failure",
            },
        ]
```

-   Note that `run_stage` converts exceptions to strings using `repr`
    -   Python doesn't implement `==` on exception objects
    -   And `str(exc)` produces the error message, not the exception class
    -   Once again, we are designing for testability
