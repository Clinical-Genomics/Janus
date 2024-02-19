"""Module that holds the parsing functionality."""
from itertools import product
from pathlib import Path

from janus.constants.workflow_models import MultiQCModels
from janus.io.read_json import read_json
from janus.models.multiqc.models import (
    PicardInsertSize,
    SamtoolsStats,
    PicardHsMetrics,
    PicardAlignmentSummary,
    SomalierIndividual,
    SomalierComparison,
    PeddyCheck,
    PicardRNASeqMetrics,
    STARAlignment, Somalier, Fastp,
)


def parse_sample_metrics(
    file_path: Path, sample_ids: list[str], metrics_model: str
) -> dict[SamtoolsStats | PicardHsMetrics | PicardInsertSize | PicardAlignmentSummary]:
    """Parse the content for a given file path into the corresponding model for each sample."""
    json_content: list[dict] = read_json(file_path)
    parsed_content: dict[SamtoolsStats | PicardHsMetrics | PicardInsertSize | PicardAlignmentSummary] = {}
    for entry, sample_id in product(json_content, sample_ids):
        if sample_id in entry:
            parsed_content[sample_id] = MultiQCModels[metrics_model].value(**json_content[entry])
    return parsed_content


def parse_somalier(file_path: Path) -> Somalier:
    """Parse the somalier multiqc file."""
    individuals: list[SomalierIndividual] = []
    comparison: SomalierComparison | None = None
    json_content: list[dict] = read_json(file_path)
    for entry in json_content:
        if entry.__contains__("*"):
            comparison = SomalierComparison(**json_content[entry])
        else:
            individuals.append(SomalierIndividual(**json_content[entry]))
    return Somalier(individuals=individuals,comparison=comparison)

def parse_fastp(file_path) -> Fastp:
    """Parse the Fastp multiqc file."""
