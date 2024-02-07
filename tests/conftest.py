"""Fixtures for the tests."""
from pathlib import Path

import pytest


@pytest.fixture
def file_fixtures() -> Path:
    return Path("fixtures", "files")

@pytest.fixture
def test_json_path(file_fixtures: Path) -> Path:
    return Path(file_fixtures, "test_json.json")


@pytest.fixture
def alignment_summary_metrics_path() -> Path:
    return Path("fixtures", "files", "picard_AlignmentSummaryMetrics.json")


@pytest.fixture
def picard_hs_metrics_path() -> Path:
    return Path("fixtures", "files", "picard_HsMetrics.json")


@pytest.fixture
def picard_insert_size_path() -> Path:
    return Path("fixtures", "files", "picard_insertSize.json")


@pytest.fixture
def samtools_stats_path() -> Path:
    return Path("fixtures", "files", "samtools_stats.json")


@pytest.fixture
def somalier_path() -> Path:
    return Path("fixtures", "files", "somalier.json")
