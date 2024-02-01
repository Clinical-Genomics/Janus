"""Tests for reading files."""
from pathlib import Path

from janus.io.read_json import read_json


def test_read_json(test_json_path: Path):
    """Test to read a JSON file."""

    # GIVEN a path to a JSON file

    # WHEN reading the JSON file
    content = read_json(test_json_path)
    # THEN the JSON file is read
    assert content

