"""Test file caching."""

from unittest.mock import patch

import pytest

from nitinat.cache import FileCache
from nitinat.exceptions import NitinatException


@pytest.fixture
def clear_cache():
    FileCache.clear()


def test_filecache_load_existing_file(clear_cache):
    cached = FileCache.get("release-count.csv")
    assert cached.is_absolute()
    with open(cached, "r") as reader:
        assert reader.readline().strip() == "Package,Releases"


def test_filecache_remote_file_doesnt_exist():
    with pytest.raises(NitinatException):
        FileCache.get("nonexistent.file")


def test_filecache_cannot_copy_remote_file(clear_cache):
    with patch("nitinat.cache.shutil.copyfile", side_effect=FileNotFoundError()):
        with pytest.raises(FileNotFoundError):
            FileCache.get("release-count.csv")


def test_filecache_copy_file_once(clear_cache):
    with patch("nitinat.cache.shutil.copyfile") as mock:
        [FileCache.get("release-count.csv") for i in range(3)]
    assert mock.call_count == 1
