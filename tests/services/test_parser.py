"""Tests for the json parser."""
from pathlib import Path

from _pytest.fixtures import FixtureRequest
import pytest

from janus.constants.FileTag import FileTag
from janus.mappers.tag_to_models import TagToModel
from janus.models.multiqc.models import (
    PicardInsertSize,
    SamtoolsStats,
    PicardHsMetrics,
    PicardAlignmentSummary,
    Fastp,
    Somalier,
)
from janus.services.parser import parse_fastp, parse_somalier, parse_sample_metrics


def test_parse_fastp(fastp_path: Path, test_sample_ids: list[str]):

    # GIVEN a file path and sample ids

    # WHEN parsing the fastp json file
    parsed_content: dict[Fastp] = parse_fastp(file_path=fastp_path, sample_ids=test_sample_ids)

    # THEN the fastp is parsed
    for entry in parsed_content:
        assert entry in test_sample_ids
        sample_metrics = parsed_content[entry]
        for metrics_tag in parsed_content[entry]:
            assert metrics_tag == FileTag.FASTP.value
            assert isinstance(sample_metrics[metrics_tag], Fastp)
            content: Fastp = sample_metrics[metrics_tag]
            assert content.after_filtering.total_reads > 0


def test_parse_somalier(somalier_path: Path):

    # GIVEN a file path

    # WHEN parsing the somalier json file
    parsed_content: dict = parse_somalier(file_path=somalier_path, case_id="testcase")

    # THEN the somalier files is parsed
    case_contents: dict = parsed_content["testcase"]
    assert isinstance(case_contents[FileTag.SOMALIER.value], Somalier)


@pytest.mark.parametrize(
    "file_path,sample_ids,tag",
    [
        ("alignment_summary_metrics_path", "test_sample_ids", "picard_alignment_summary_tag"),
        ("picard_hs_metrics_path", "test_sample_ids", "picard_hs_metrics_tag"),
        ("picard_insert_size_path", "test_sample_ids", "picard_insert_size_tag"),
        ("samtools_stats_path", "test_sample_ids", "samtools_stats_tag"),
        ("picard_wgs_metrics_path", "test_sample_ids", "picard_wgs_metrics_tag"),
        ("picard_dups_path", "test_sample_ids", "picard_dups_tag"),
    ],
)
def test_parse_sample_metrics(file_path: str, sample_ids: str, tag: str, request: FixtureRequest):

    # GIVEN a file path, sample ids and a metrics model
    file_path: Path = request.getfixturevalue(file_path)
    sample_ids: list[str] = request.getfixturevalue(sample_ids)
    tag: str = request.getfixturevalue(tag)
    # WHEN parsing the specified metrics model
    parsed_content: dict[
        SamtoolsStats | PicardHsMetrics | PicardInsertSize | PicardAlignmentSummary
    ] = parse_sample_metrics(file_path=file_path, sample_ids=sample_ids, tag=tag)

    # THEN the content is parsed
    for entry in parsed_content:
        assert entry in sample_ids
        sample_metrics = parsed_content[entry]
        for metrics_tag in parsed_content[entry]:
            assert tag == metrics_tag
            content: SamtoolsStats | PicardHsMetrics | PicardInsertSize | PicardAlignmentSummary = (
                sample_metrics[metrics_tag]
            )
            assert isinstance(content, TagToModel[tag].value)
