"""Module to hold the collect qc service."""
from janus.constants.workflow_models import WorkflowSampleModels
from janus.dto.collect_qc_request import CollectQCRequest
from janus.models.workflow.models import BalsamicWGSSample, BalsamicTGASample


def get_model_name(workflow: str, prep_category: str) -> str:
    """
    Get the model name from workflow and prep category.
    NOTE: Balsamic samples cannot uniquely be identified by workflow only.
    """
    return f"{workflow}_{prep_category}".upper() if workflow == "balsamic" else workflow.upper()


def get_sample_model(
    workflow: str, prep_category: str | None
) -> BalsamicTGASample | BalsamicWGSSample:
    """Return the sample model for a workflow and prep category if specified."""
    model_name: str = get_model_name(workflow=workflow, prep_category=prep_category)
    for workflow_sample_model in WorkflowSampleModels:
        if workflow_sample_model.name == model_name:
            return workflow_sample_model.value


def add_sample_id_to_model(
    sample_ids: list[str], sample_model: type[BalsamicWGSSample | BalsamicTGASample]
):
    """Add a sample id to the sample model."""
    samples: list[BalsamicWGSSample | BalsamicWGSSample] = []
    for sample_id in sample_ids:
        sample = sample_model
        sample.sample_id = sample_id
        samples.append(sample)
    return samples


def prepare_sample_models(collect_qc_request: CollectQCRequest):
    """Prepare sample model list to which the multiqc files have to be parsed."""
    sample_model: BalsamicWGSSample | BalsamicTGASample = get_sample_model(
        workflow=collect_qc_request.workflow, prep_category=collect_qc_request.prep_category
    )
    samples: list[BalsamicWGSSample | BalsamicTGASample] = add_sample_id_to_model(
        sample_ids=collect_qc_request.samples, sample_model=sample_model
    )
    return samples


def collect_qc_for_sample(collect_qc_request: CollectQCRequest):
    """Collect the qc metrics for a sample."""
    # For every sample
