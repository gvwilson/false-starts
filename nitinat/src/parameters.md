---
title: Handling Model Parameters
---

-   Parameters for real machine learning models are large enough to be worth caching
-   Pretend to do it with a top-level directory called `parameters` that holds JSON files
    -   Instead of remote files
-   A new file `nitinat/parameters.py` that implements a cache for parameter objects
    -   Any particular object is created at most once during the lifetime of the program
-   Some examples of actual model parameter objects
    -   Use [pydantic][pydantic] to manage these
    -   Real ones will be far more complex, but this gives us an opportunity to introduce pydantic
-   Add the path to the parameter file directory to `CONFIG` in `__init__.py`

```python
CONFIG = {
    ...previous values...
    "PARAMETERS": Path(__file__).parent.parent.joinpath("parameters")
}
```

-   Then implement the cache

```python
class Parameters:
    """Instantiate model parameters with caching."""

    # (class, filename) => object
    _cache = {}

    @staticmethod
    def get(cls, filename):
        """Return model parameters object with caching."""
        if (cls, filename) not in Parameters._cache:
            path = Path(CONFIG["PARAMETERS"], filename)
            with open(path, "r") as reader:
                values = Parameters._load_json(path)
                Parameters._cache[(cls, filename)] = cls(**values)
        return Parameters._cache[(cls, filename)]
```

-   Test that an actual file loads correctly

```python
def test_parameters_fraction_load():
    parameters = Parameters.get(FractionSelectorParameters, "fraction-0.1.json")
    assert parameters.fraction == 0.1
```

-   Test that a given object is only instantiated once

```python
def test_parameters_objects_are_recycled():
    parameters = [Parameters.get(NthSelectorParameters, "nth-50.json") for i in range(3)]
    assert all(id(p) == id(parameters[0]) for p in parameters)
```

-   Use the fact that every object in Python has a unique ID (location in memory)
-   Test that a file containing an invalid value fails as it should
    -   But don't want to create bad files in parameter file directory
    -   Or override the directory
    -   So refactor the cache to put exactly the code we want to patch in a method of its own

```python
@staticmethod
def get(cls, filename):
    """Return model parameters object with caching."""
    if (cls, filename) not in Parameters._cache:
        path = Path(CONFIG["PARAMETERS"], filename)
        values = Parameters._load_json(path)
        Parameters._cache[(cls, filename)] = cls(**values)
    return Parameters._cache[(cls, filename)]

@staticmethod
def _load_json(path):
    with open(path, "r") as reader:
        return json.load(reader)
```

-   A two-line method to open a file and read JSON might seem unnecessary
    -   But this is what we mean by "design for test"
-   The test is now easy to write:

```python
LOAD_JSON = "nitinat.parameters.Parameters._load_json"

def test_parameters_fraction_invalid_negative():
    with patch(LOAD_JSON, return_value={"fraction": -0.1}):
        with pytest.raises(ValueError):
            Parameters.get(FractionSelectorParameters, "fraction.json")
```

-   Let's make sure that we really do load the JSON parameter file only once

```python
def test_parameters_load_called_once():
    with patch(LOAD_JSON, return_value={"stride": 50}) as mock:
        [Parameters.get(NthSelectorParameters, "nth-50.json") for i in range(3)]
    assert mock.call_count == 1
```

-   `patch` creates a [mock object][python-mock]
    -   We can ask it questions like "how many times were you called?"
-   Run this test on its own with `pytest -k test_parameters_load_called_once`
    -   It passes!
    -   Add issue #7: find a way to pass flags to `pytest` when using Invoke
-   Run the whole test suite: this test fails
    -   Look at output: our mock object is called 0 times
    -   Because other tests have already loaded this file, so the cache is doing what it's supposed to
-   Solution: clear the cache between each test run
    -   Add this to `nitinat/parameters.py`

```python
@staticmethod
def clear():
    Parameters._cache.clear()
```

-   Add this to `tests/conftest.py` (stands for "configure tests")

```python
@fixture
def clear_cache():
    Parameters.clear()
```

-   A "fixture" that we use for its side effect
    -   Modify the test to use this fixture

```python
def test_parameters_load_called_once(clear_cache):
    with patch(LOAD_JSON, return_value={"stride": 50}) as mock:
        [Parameters.get(NthSelectorParameters, "nth-50.json") for i in range(3)]
    assert mock.call_count == 1
```

-   And now it works
