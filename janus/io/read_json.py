"""Read JSON module"""
import json
from pathlib import Path


def read_json(file_path: Path) -> any:
    """Read content in a json file."""
    with open(file_path, "r") as file:
        return json.load(file)
