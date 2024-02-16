"""Module to hold the collect qc service."""
from janus.dto.collect_qc_request import CollectQCRequest
from janus.models.workflow.models import BalsamicWGSSample, BalsamicTGASample


def get_sample_model(
    workflow: str, prep_category: str | None
) -> BalsamicTGASample | BalsamicTGASample:
    """Return the sample model for a workflow and prep category if specified."""
    pass


def add_sample_id_to_model(
    sample_ids: list[str], sample_model: BalsamicWGSSample | BalsamicTGASample
):
    """Add a sample id to the sample model."""
    pass


def prepare_sample_models(collect_qc_request: CollectQCRequest):
    """Prepare sample model list to which the multiqc files have to be parsed."""
    sample_model: BalsamicWGSSample | BalsamicTGASample = get_sample_model(
        workflow=collect_qc_request.workflow, prep_category=collect_qc_request.prep_category
    )
    samples: list[BalsamicWGSSample | BalsamicTGASample] = add_sample_id_to_model(
        sample_ids=collect_qc_request.samples, sample_model=sample_model
    )
    return samples


def collect_qc_for_sample():

    pass
