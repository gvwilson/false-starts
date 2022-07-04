"""Check that the project has a heartbeat."""

import nitinat


def test_module_can_be_imported():
    assert hasattr(nitinat, "__author__")
    assert hasattr(nitinat, "__version__")
