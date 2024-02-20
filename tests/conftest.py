"""Fixtures for the tests."""
from pathlib import Path

import pytest

from janus.dto.collect_qc_request import CollectQCRequest


# Parser


@pytest.fixture
def file_fixtures() -> Path:
    return Path("fixtures", "files")


@pytest.fixture
def test_json_path(file_fixtures: Path) -> Path:
    return Path(file_fixtures, "test_json.json")


@pytest.fixture
def fastp_path(file_fixtures: Path) -> Path:
    return Path(file_fixtures, "fastp.json")


@pytest.fixture
def alignment_summary_metrics_path(file_fixtures: Path) -> Path:
    return Path(file_fixtures, "picard_AlignmentSummaryMetrics.json")


@pytest.fixture
def picard_hs_metrics_path(file_fixtures: Path) -> Path:
    return Path("fixtures", "files", "picard_HsMetrics.json")


@pytest.fixture
def picard_insert_size_path(file_fixtures: Path) -> Path:
    return Path(file_fixtures, "picard_insertSize.json")


@pytest.fixture
def samtools_stats_path(file_fixtures: Path) -> Path:
    return Path(file_fixtures, "samtools_stats.json")


@pytest.fixture
def somalier_path(file_fixtures: Path) -> Path:
    return Path(file_fixtures, "somalier.json")


@pytest.fixture
def test_sample_ids() -> list[str]:
    return ["testsampleA", "testsampleB"]


# Collect qc service
@pytest.fixture
def balsamic_workflow() -> str:
    return "balsamic"


@pytest.fixture
def wgs_prep_category() -> str:
    return "wgs"


@pytest.fixture
def collect_qc_request() -> CollectQCRequest:
    return CollectQCRequest(
        case_id="example_case_id",
        sample_ids=["sample1", "sample2"],
        file_names=["file1.txt", "file2.txt"],
        workflow="balsamic",
        prep_category="tga",
    )
