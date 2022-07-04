"""Simulate a file cache."""

import shutil
from pathlib import Path

from . import CONFIG
from .exceptions import NitinatException


class FileCache:
    """Cache large remote files."""

    # Map remote filenames to local cached filenames.
    _cache = {}

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

    @classmethod
    def clear(cls):
        """Clear the cache, deleting local files."""
        cls._cache.clear()
        for filename in CONFIG["cache"].iterdir():
            filename.unlink()
