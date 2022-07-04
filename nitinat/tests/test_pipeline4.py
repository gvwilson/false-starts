"""Test layered configuration pipeline."""

from pathlib import Path
from unittest.mock import patch

import yaml

from nitinat.pipeline4 import SYSTEM_CONFIG, read_layered_config

GET_HOME_DIR = "nitinat.pipeline4._get_home_dir"


def make_file(fs, path, contents):
    fs.create_file(path, contents=yaml.dump(contents))


def test_layered_config_read_system(fs):
    fs.cwd = "/home/person/project/analysis"
    expected = {"alpha": 1}
    make_file(fs, SYSTEM_CONFIG, expected)
    with patch(GET_HOME_DIR, return_value=Path("/home/person")):
        actual = read_layered_config("test.yml")
    assert actual == expected


def test_layered_config_read_personal(fs):
    fs.cwd = "/home/person/project/analysis"
    expected = {"beta": 2}
    make_file(fs, "/home/person/.nitinat.yml", expected)
    with patch(GET_HOME_DIR, return_value=Path("/home/person")):
        actual = read_layered_config("test.yml")
    assert actual == expected


def test_layered_config_read_project_from_project_root(fs):
    fs.cwd = "/home/person/project/analysis"
    expected = {"gamma": 3}
    make_file(fs, "/home/person/project/.nitinat.yml", expected)
    with patch(GET_HOME_DIR, return_value=Path("/home/person")):
        actual = read_layered_config("test.yml")
    assert actual == expected


def test_layered_config_read_project_from_project_subdir(fs):
    fs.cwd = "/home/person/project/analysis"
    expected = {"gamma": 3}
    make_file(fs, "/home/person/project/.nitinat.yml", expected)
    with patch(GET_HOME_DIR, return_value=Path("/home/person")):
        actual = read_layered_config("temp/test.yml")
    assert actual == expected


def test_layered_config_combine_files(fs):
    fs.cwd = "/home/person/project/analysis"
    make_file(fs, SYSTEM_CONFIG, {"alpha": 1})
    make_file(fs, "/home/person/.nitinat.yml", {"beta": 2})
    make_file(fs, "/home/person/project/.nitinat.yml", {"gamma": 3})
    with patch(GET_HOME_DIR, return_value=Path("/home/person")):
        actual = read_layered_config("temp/test.yml")
    assert actual == {"alpha": 1, "beta": 2, "gamma": 3}
