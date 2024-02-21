"""Module to hold the collect qc service."""

from janus.dto.collect_qc_request import CollectQCRequest, FilePathAndTag
from janus.mappers.tag_to_parse_function import TagToParseFunction
from janus.mappers.workflow_to_tag import WorkflowToTag
from janus.mappers.workflow_to_sample_model import WorkflowToSampleModel
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
    return WorkflowToSampleModel[model_name].value


def get_workflow_models(workflow: str, prep_category: str) -> list[str]:
    model_name: str = get_model_name(workflow=workflow, prep_category=prep_category)
    for workflow in WorkflowToTag:
        if workflow.name == model_name:
            return workflow.value


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
        sample_ids=collect_qc_request.sample_ids, sample_model=sample_model
    )
    return samples


def collect_metrics_for_models(
    file_paths_and_tags: list[FilePathAndTag], sample_ids: list[str]
) -> list[dict]:
    """Return a list of parse functions."""
    collected_metrics: list[callable] = []
    for file_path_and_tag in file_paths_and_tags:
        test = TagToParseFunction
        parse_function = TagToParseFunction[file_path_and_tag.tag].value
        collected_metrics.append(
            parse_function(
                file_path=file_path_and_tag.file_path,
                sample_ids=sample_ids,
                tag=file_path_and_tag.tag,
            )
        )
    return collected_metrics


def collect_qc(collect_qc_request: CollectQCRequest):
    """Collect the qc metrics for a sample."""

    collected_metrics: list[dict] = collect_metrics_for_models(
        file_paths_and_tags=collect_qc_request.files, sample_ids=collect_qc_request.sample_ids
    )

    # parse the data
    parsed_metrics: list[dict] = []

    # get the prepared sample models

    # put the data into the proper sample models

    # generate collect qc response
