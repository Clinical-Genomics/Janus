"""Fixtures for the tests."""
from pathlib import Path

import pytest


@pytest.fixture
def test_json_path() -> Path:
    return Path("fixtures", "files", "test_json.json")
