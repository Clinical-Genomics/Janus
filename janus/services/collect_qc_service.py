"""Module to hold the collect qc service."""

from janus.dto.collect_qc_request import CollectQCRequest, FilePathAndTag
from janus.mappers.tag_to_parse_function import tag_to_parse_function

from janus.mappers.workflow_to_model import WorkflowToModel
from janus.mappers.workflow_to_sample_model import WorkflowToSampleModel
from janus.models.workflow.models import BalsamicWGSSample, BalsamicTGASample, Balsamic


def get_sample_model_name(workflow: str, prep_category: str) -> str:
    """
    Get the model name from workflow and prep category.
    NOTE: Balsamic samples cannot uniquely be identified by workflow only.
    """
    return f"{workflow}_{prep_category}".upper() if workflow == "balsamic" else workflow.upper()


def get_sample_model(
    workflow: str, prep_category: str | None
) -> BalsamicTGASample | BalsamicWGSSample:
    """Return the sample model for a workflow and prep category if specified."""
    model_name: str = get_sample_model_name(workflow=workflow, prep_category=prep_category)
    return WorkflowToSampleModel[model_name].value


def get_workflow_models(workflow: str) -> Balsamic:
    """Return the model for a workflow."""
    return WorkflowToModel[workflow].value


def collect_metrics_for_models(collect_qc_request: CollectQCRequest,
) -> list[dict]:
    """Return a list of parse functions."""
    collected_metrics: list[callable] = []
    for file_path_and_tag in collect_qc_request.files:
        parse_function = tag_to_parse_function[file_path_and_tag.tag]
        collected_metrics.append(
            parse_function(
                file_path=file_path_and_tag.file_path,
                sample_ids=collect_qc_request.sample_ids,
                tag=file_path_and_tag.tag,
                case_id=collect_qc_request.case_id
            )
        )
    return collected_metrics


def get_collected_metrics_for_sample(collected_metrics: list[dict], sample_id: str) -> dict:
    sample_metrics: dict = {"sample_id" : sample_id}
    for collected_metric in collected_metrics:
        for metric_tag, metric in collected_metric.items():
            if metric_tag == sample_id:
                sample_metrics[metric_tag] = metric
    return sample_metrics

def collect_qc(collect_qc_request: CollectQCRequest):
    """Collect the qc metrics for a samples."""
    collected_metrics: list[dict] = collect_metrics_for_models(
        file_paths_and_tags=collect_qc_request.files, sample_ids=collect_qc_request.sample_ids
    )
    # get the prepared sample models
    sample_model: BalsamicWGSSample | BalsamicTGASample = get_sample_model(workflow=collect_qc_request.workflow,prep_category=collect_qc_request.prep_category)
    workflow_samples: list[BalsamicWGSSample | BalsamicTGASample] = []
    for sample_id in collect_qc_request.sample_ids:
        collected_sample_metrics: dict = get_collected_metrics_for_sample(collected_metrics=collected_metrics, sample_id=sample_id)
        collected_sample_metrics_model: BalsamicWGSSample | BalsamicTGASample = sample_model(**collected_sample_metrics)
        workflow_samples.append(collected_sample_metrics_model)


