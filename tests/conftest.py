"""Fixtures for the tests."""
from pathlib import Path

import pytest

from janus.mappers.mappers import MultiQCModels
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


@pytest.fixture
def picard_hs_metrics_name():
    return MultiQCModels.PICARD_HS_METRICS.name


@pytest.fixture
def picard_wgs_metrics_name():
    return MultiQCModels.PICARD_WGS_METRICS.name


@pytest.fixture
def picard_dups_name():
    return MultiQCModels.PICARD_DUPS.name


@pytest.fixture
def picard_insert_size_name():
    return MultiQCModels.PICARD_INSERT_SIZE.name


@pytest.fixture
def picard_alignment_summary_name():
    return MultiQCModels.PICARD_ALIGNMENT_SUMMARY.name


@pytest.fixture
def fastp_name():
    return MultiQCModels.FASTP.name


@pytest.fixture
def peddy_check_name():
    return MultiQCModels.PEDDY_CHECK.name


@pytest.fixture
def somalier_name():
    return MultiQCModels.SOMALIER.name


@pytest.fixture
def picard_rna_seq_metrics_name():
    return MultiQCModels.PICARDRNASEQMETRICS.name


@pytest.fixture
def star_alignment_name():
    return MultiQCModels.STARALIGNMENT.name


@pytest.fixture
def rna_fusion_general_stats_name():
    return MultiQCModels.RNAFUSIONGENERALSTATS.name


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
