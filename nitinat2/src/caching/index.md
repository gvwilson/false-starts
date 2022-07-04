---
title: "Caching"
---

-   Datasets for real analysis projects are often too large to put in Git
-   Simulate this by creating two directories in our project
    -   `remote` holds the "remote" files (which we will actually keep in version control)
    -   `cache` holds the local copies of those files that we do *not* put in version control
-   A new file `nitinat/cache.py` implements a cache for files
    -   Files are only copied from `remote` to `cache` if they're not already in the latter
-   Add these values to a dictionary `CONFIG` in `nitinat/__init__.py`
    -   [% x configuration %] discusses how to make this configurable

```{.python title="nitinat/__init__.py"}
from pathlib import Path

CONFIG = {
    "cache": Path(__file__).parent.parent.joinpath("cache"),
    "remote": Path(__file__).parent.parent.joinpath("remote"),
}
```

-   Then implement the first version of the cache
    -   Use a [% g class_method "class method" %]
        rather than a [% g static_method "static method" %]
	because we might want to derive other caching classes from this one,
	and we want to be sure we're referring to the right cache if we do
    -   Use an [% g absolute_path "absolute path" %] for the cached file
        because relative paths will be unreliable once we start configuring directories

```{.python title="nitinat/parameters.py"}
from pathlib import Path
import shutil

from . import CONFIG


class FileCache:
    """Cache large remote files."""

    # Map remote filenames to local cached filenames.
    _cache = {}

    @classmethod
    def get(cls, filename):
        """Return path to cached copy of file, getting as needed."""
        if filename not in cls._cache:
            remote_path = Path(CONFIG["remote"], filename)
            cache_path = Path(CONFIG["cache"], filename).resolve()
            shutil.copyfile(remote_path, cache_path)
            cls._cache[filename] = cache_path
        return cls._cache[filename]
```

-   Move our existing dataset to the `remote` directory
-   Test that we can load it by creating `tests/test_parameters.py` and adding this

```{.python title="tests/test_cache.py"}
from nitinat.cache import FileCache


def test_filecache_load_existing_file():
    cached = FileCache.get("release-count.csv")
    assert cached.is_absolute()
    with open(cached, "r") as reader:
        assert reader.readline().strip() == "Package,Releases"
```

-   We should test that the desired file exists and that copying worked
-   It's OK for `shutil.copyfile` to throw `FileNotFoundError` etc.
    -   Our own exceptions are unlikely to be more informative
-   But once we start using an actual remote cache,
    we should have something of our own for "can't find what you asked for"
-   Create `nitinat/exceptions.py`

```{.python title="nitinat/exceptions.py"}
"""Create our own exceptions."""

class NitinatException(Exception):
    """Something went wrong in the Nitinat package."""

    def __init__(self, msg=""):
        """Remember what went wrong."""
        self.msg = msg

    def __repr__(self):
        """Printable."""
        msg = self.msg if self.msg else "-no message-"
        return f"<exc {msg}>"
```

-   Modify the cache

```{.python title="nitinat/cache.py"}
    @classmethod
    def get(cls, filename):
        """Return path to cached copy of file, getting as needed."""
        if filename not in cls._cache:
            remote_path = Path(CONFIG["remote"], filename)
            if not remote_path.exists():
                raise NitinatException(f"No remote file {filename}")
            cache_path = Path(CONFIG["cache"], filename)
            shutil.copyfile(remote_path, cache_path)
            cls._cache[filename] = cache_path
        return cls._cache[filename]
```

-   Test that a nonexistent file can't be found

```{.python title="tests/test_cache.py"}
import pytest
from nitinat.exceptions import NitinatException

def test_filecache_remote_file_doesnt_exist():
    with pytest.raises(NitinatException):
        FileCache.get("nonexistent.file")
```

-   Rely on mocking to test `shutil.copyfile` failure *without* actually copying a file

```{.python title="tests/test_cache.py"}
def test_filecache_cannot_copy_remote_file():
    with patch("nitinat.cache.shutil.copyfile", side_effect=FileNotFoundError()):
        with pytest.raises(FileNotFoundError):
            FileCache.get("release-count.csv")
```

-   Test fails: exception isn't raised
-   After some head-scratching realize that:
    -   The test that actually copies a file is running first
    -   So the file is in the cache by the time the second test runs
    -   So the mock of `shutil.copyfile` isn't called
-   This is why tests shouldn't have side effects...
-   Give `FileCache` a `clear` method that clears the cache in memory and deletes files on disk


```{.python title="nitinat/cache.py"}
    @classmethod
    def clear(cls):
        """Clear the cache, deleting local files."""
        cls._cache.clear()
        for filename in CONFIG["cache"].iterdir():
            filename.unlink()
```

-   Use a fixture to clear the cache
    -   Because fixtures can depend on other fixtures,
        but each fixture is only "created" (called) once

```{.python title="tests/test_cache.py"}
@pytest.fixture
def clear_cache():
    FileCache.clear()
```

-   Rewrite test to include fixture
    -   Value will be `None`, since the `clear_cache` function doesn't return anything
    -   But it guarantees the cache is empty by the time the test function runs

```{.python title="tests/test_cache.py"}
def test_filecache_cannot_copy_remote_file(clear_cache):
    with patch("nitinat.cache.shutil.copyfile", side_effect=FileNotFoundError()):
        with pytest.raises(FileNotFoundError):
            FileCache.get("release-count.csv")
```

-   Now test that a given file is only copied once

```python
def test_filecache_copy_file_once(clear_cache):
    with patch("nitinat.cache.shutil.copyfile") as mock:
        [FileCache.get("release-count.csv") for i in range(3)]
    assert mock.call_count == 1
```

-   Mock objects remember how many times they were called
-   Run this test on its own with `pytest -k test_filecache_copy_file_once`: it passes
-   Run the whole test suite: everything else passes too
-   Add the `cache` directory to `.gitignore`
    -   The whole point of this exercise was to avoid caching large files
-   Really should replace the `exists` calls as well so that tests don't depend on particular datafiles
-   And revisit the data download script

<div class="callout" markdown="1">
### DVC

Many tools to manage files that are too large (or too sensitive) to go in Git already exist,
including [Git LFS][git_lfs] and and the newer and more versatile [DVC][dvc].
In brief, DVC works as follows:

1.  The user runs `dvc init` once in a local Git repository to create some configuration files,
    and then <code>dvc remote add -d <em>name</em> <em>url</em></code>
    to tell DVC where large files are actually stored.

1.  The command <code>dvc add <em>filename</em></code> adds the specified file to `.gitignore`
    so that it won't be saved by Git.
    It also creates a small file <code><em>filename</em>.dvc</code> that *can* be added to Git;
    this file keeps track of which version of the actual file was used.

1.  `dvc push` and `dvc pull` will send large files to remote storage or download them
    based on the IDs stored in the local `.dvc` files.

1.  Any number of repositories can refer to the same large file without any of them storing it
    so long as their DVC remotes point at the same remote storage location.

The extra steps aren't completely invisible to users---people still have to
use `dvc pull` to get the latest version of a remote large file
before trying to read it with `pandas.read_csv`, for example---but
it is simple, versatile, and free.
</div>
