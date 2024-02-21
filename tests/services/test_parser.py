"""Tests for the json parser."""
from pathlib import Path

from _pytest.fixtures import FixtureRequest
import pytest

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
        assert isinstance(parsed_content[entry], Fastp)
        content: Fastp = parsed_content[entry]
        assert content.after_filtering.total_reads > 0


def test_parse_somalier(somalier_path: Path):

    # GIVEN a file path

    # WHEN parsing the somalier json file
    parsed_content: dict = parse_somalier(file_path=somalier_path, case_id="testcase")

    # THEN the somalier files is parsed
    assert isinstance(parsed_content["testcase"], Somalier)


@pytest.mark.parametrize(
    "file_path,sample_ids,metrics_model",
    [
        ("alignment_summary_metrics_path", "test_sample_ids", "picard_alignment_summary_tag"),
        ("picard_hs_metrics_path", "test_sample_ids", "picard_hs_metrics_tag"),
        ("picard_insert_size_path", "test_sample_ids", "picard_insert_size_tag"),
        ("samtools_stats_path", "test_sample_ids", "samtools_stats_tag"),
        ("picard_wgs_metrics_path", "test_sample_ids", "picard_wgs_metrics_tag"),
        ("picard_dups_path", "test_sample_ids", "picard_dups_tag"),
    ],
)
def test_parse_sample_metrics(
    file_path: str, sample_ids: str, metrics_model: str, request: FixtureRequest
):

    # GIVEN a file path, sample ids and a metrics model
    file_path: Path = request.getfixturevalue(file_path)
    sample_ids: list[str] = request.getfixturevalue(sample_ids)
    metrics_model: str = request.getfixturevalue(metrics_model)
    # WHEN parsing the specified metrics model
    parsed_content: dict[
        SamtoolsStats | PicardHsMetrics | PicardInsertSize | PicardAlignmentSummary
    ] = parse_sample_metrics(file_path=file_path, sample_ids=sample_ids, tag=metrics_model)

    # THEN the content is parsed
    for entry in parsed_content:
        assert entry in sample_ids
        content: SamtoolsStats | PicardHsMetrics | PicardInsertSize | PicardAlignmentSummary = (
            parsed_content[entry]
        )
        assert isinstance(content, TagToModel[metrics_model].value)



