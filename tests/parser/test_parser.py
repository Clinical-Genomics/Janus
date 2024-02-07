"""Tests for the json parser."""
from pathlib import Path
from _pytest.fixtures import FixtureRequest
import pytest

from janus.io.read_json import read_json

from janus.parser.parser import parse_json
from janus.models.multiqc.models import (
    PicardInsertSize,
    SamtoolsStats,
    PicardHsMetrics,
    PicardAlignmentSummary,
)


@pytest.mark.parametrize(
    "mutliqc_json_path, model",
    [
        ("samtools_stats_path", SamtoolsStats),
        ("alignment_summary_metrics_path", PicardAlignmentSummary),
        ("picard_hs_metrics_path", PicardHsMetrics),
        ("picard_insert_size_path", PicardInsertSize),
    ],
)
def test_parse_json(
    mutliqc_json_path: str,
    model: type[
        SamtoolsStats | PicardAlignmentSummary | PicardHsMetrics | PicardInsertSize
    ],
    request: FixtureRequest,
):
    """Test the parsing of different multiqc json files into the multiqcmodel."""
    # GIVEN a path to an intermediate multiqc json file

    # WHEN parsed the read content
    content = read_json(file_path=request.getfixturevalue(mutliqc_json_path))

    # THEN an appropriate model is returned
    parsed_content: list = parse_json(content)
    assert parsed_content
    for content in parsed_content:
        assert isinstance(content, model)
