"""Module that holds the parsing functionality."""
from pydantic_core._pydantic_core import ValidationError

from janus.exceptions.exceptions import ParseJSONError
from janus.models.multiqc.models import (
    PicardInsertSize,
    SamtoolsStats,
    PicardHsMetrics,
    PicardAlignmentSummary,
    SomalierIndividual,
    SomalierComparison,
    PeddyCheck,
    PicardRNASeqMetrics,
    STARAlignment,
)

models = [
    PicardInsertSize,
    SamtoolsStats,
    PicardHsMetrics,
    PicardAlignmentSummary,
    SomalierIndividual,
    SomalierComparison,
    PeddyCheck,
    PicardRNASeqMetrics,
    STARAlignment,
]


def parse_json(content: any):
    """
    Parse the json content into multiqc models.
         Raises: ...
     """
    parsed_content = []
    for entry in content:
        for model in models:
            entry_content = content[entry]
            try:
                parsed_content.append(model.model_validate(entry_content))
            except ValidationError as e:
                pass
    if not parsed_content:
        raise ParseJSONError(f"Failed to parse JSON file.")
    return parsed_content
