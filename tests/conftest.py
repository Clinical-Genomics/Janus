"""Fixtures for the tests."""

from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest

from janus.constants.FileTag import FileTag
from janus.constants.workflow import Workflow
from janus.dto.collect_qc_request import CollectQCRequest, FilePathAndTag, WorkflowInfo
from janus.services.collect_qc_service import CollectQCService


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
def picard_wgs_metrics_path(file_fixtures: Path) -> Path:
    return Path("fixtures", "files", "picard_wgsMetrics.json")


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
def picard_dups_path(file_fixtures: Path) -> Path:
    return Path(file_fixtures, "picard_dups.json")


@pytest.fixture
def test_sample_ids() -> list[str]:
    return ["testsampleA", "testsampleB"]


@pytest.fixture
def picard_hs_metrics_tag() -> str:
    return FileTag.HS_METRICS


@pytest.fixture
def picard_wgs_metrics_tag() -> str:
    return FileTag.WGS_METRICS


@pytest.fixture
def picard_dups_tag() -> str:
    return FileTag.DUPLICATES


@pytest.fixture
def samtools_stats_tag() -> str:
    return FileTag.SAMTOOLS_STATS


@pytest.fixture
def picard_insert_size_tag() -> str:
    return FileTag.INSERT_SIZE


@pytest.fixture
def picard_alignment_summary_tag() -> str:
    return FileTag.ALIGNMENT_SUMMARY_METRICS


@pytest.fixture
def fastp_tag() -> str:
    return FileTag.FASTP


@pytest.fixture
def somalier_tag() -> str:
    return FileTag.SOMALIER


@pytest.fixture
def star_alignment_tag() -> str:
    return FileTag.STAR_ALIGNMENT


@pytest.fixture
def rna_fusion_general_stats_tag() -> str:
    return "RNAFUSIONGENERALSTATS"


# Collect qc service
@pytest.fixture
def balsamic_workflow() -> str:
    return "balsamic"


@pytest.fixture
def test_file_tag_model() -> FilePathAndTag:
    return FilePathAndTag(file_path="test_path", tag="test_tag")


@pytest.fixture
def test_case_id() -> str:
    return "test_case"


@pytest.fixture
def collect_qc_request(
    test_file_tag_model: FilePathAndTag, test_case_id: str
) -> CollectQCRequest:
    return CollectQCRequest(
        case_id=test_case_id,
        sample_ids=["sample1", "sample2"],
        files=[test_file_tag_model],
        workflow="balsamic",
    )


@pytest.fixture
def balsamic_files_wgs(request: FixtureRequest) -> list[FilePathAndTag]:
    fixtures: dict = {
        "alignment_summary_metrics_path": "picard_alignment_summary_tag",
        "picard_hs_metrics_path": "picard_hs_metrics_tag",
        "picard_dups_path": "picard_dups_tag",
        "picard_wgs_metrics_path": "picard_wgs_metrics_tag",
        "picard_insert_size_path": "picard_insert_size_tag",
        "somalier_path": "somalier_tag",
        "fastp_path": "fastp_tag",
        "samtools_stats_path": "samtools_stats_tag",
    }

    file_path_tags: dict = {
        request.getfixturevalue(key): request.getfixturevalue(value)
        for key, value in fixtures.items()
    }

    files: list[FilePathAndTag] = []
    for key, value in file_path_tags.items():
        files.append(FilePathAndTag(file_path=str(key), tag=value))
    return files


@pytest.fixture
def balsamic_files_tga(request: FixtureRequest) -> list[FilePathAndTag]:
    fixtures: dict = {
        "alignment_summary_metrics_path": "picard_alignment_summary_tag",
        "picard_hs_metrics_path": "picard_hs_metrics_tag",
        "picard_dups_path": "picard_dups_tag",
        "picard_insert_size_path": "picard_insert_size_tag",
        "somalier_path": "somalier_tag",
        "fastp_path": "fastp_tag",
        "samtools_stats_path": "samtools_stats_tag",
    }

    file_path_tags: dict = {
        request.getfixturevalue(key): request.getfixturevalue(value)
        for key, value in fixtures.items()
    }

    files: list[FilePathAndTag] = []
    for key, value in file_path_tags.items():
        files.append(FilePathAndTag(file_path=str(key), tag=value))
    return files


@pytest.fixture
def collect_qc_request_balsamic_wgs(
    balsamic_files_wgs: list[FilePathAndTag],
    test_sample_ids: list[str],
    test_case_id: str,
) -> CollectQCRequest:
    return CollectQCRequest(
        case_id=test_case_id,
        sample_ids=test_sample_ids,
        files=balsamic_files_wgs,
        workflow_info=WorkflowInfo(workflow=Workflow.BALSAMIC.value, version="0"),
    )


@pytest.fixture
def collect_qc_request_balsamic_tga(
    balsamic_files_tga: list[FilePathAndTag],
    test_sample_ids: list[str],
    test_case_id: str,
) -> CollectQCRequest:
    return CollectQCRequest(
        case_id=test_case_id,
        sample_ids=test_sample_ids,
        files=balsamic_files_tga,
        workflow_info=WorkflowInfo(workflow=Workflow.BALSAMIC.value, version="0"),
    )


@pytest.fixture
def collect_balsamic_qc_service_wgs(
    collect_qc_request_balsamic_wgs: CollectQCRequest,
) -> CollectQCService:
    return CollectQCService(collect_qc_request_balsamic_wgs)


@pytest.fixture
def collect_balsamic_qc_service_tga(
    collect_qc_request_balsamic_tga: CollectQCRequest,
) -> CollectQCService:
    return CollectQCService(collect_qc_request_balsamic_tga)


@pytest.fixture
def collect_qc_service_unsupported_workflow(
    collect_qc_request_balsamic_wgs: CollectQCRequest,
) -> CollectQCService:
    request: CollectQCRequest = collect_qc_request_balsamic_wgs
    request.workflow_info.workflow = "not_supported"
    return CollectQCService(request)
