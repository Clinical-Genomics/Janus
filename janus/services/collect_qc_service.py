"""Module to hold the collect qc service."""
from janus.constants.FileTag import FileTag
from janus.dto.collect_qc_request import CollectQCRequest
from janus.mappers.tag_to_parse_function import tag_to_parse_function
from janus.models.workflow.models import Balsamic


def collect_metrics(
    collect_qc_request: CollectQCRequest,
) -> list[dict]:
    """Collect the metrics for the files provided in the request."""
    collected_metrics: list[callable] = []
    for file_path_and_tag in collect_qc_request.files:
        parse_function = tag_to_parse_function[file_path_and_tag.tag]
        collected_metrics.append(
            parse_function(
                file_path=file_path_and_tag.file_path,
                sample_ids=collect_qc_request.sample_ids,
                tag=file_path_and_tag.tag,
                case_id=collect_qc_request.case_id,
            )
        )
    return collected_metrics


def format_sample_metrics(collected_metrics: list[dict], sample_id: str) -> dict:
    """Format the metrics for a sample."""
    sample_metrics: dict = {"sample_id": sample_id}
    for collected_metric in collected_metrics:
        for metric_tag, metric in collected_metric.items():
            if metric_tag == sample_id:
                sample_metrics[metric_tag] = metric
    return sample_metrics


def get_formatted_sample_metrics(collected_metrics: list[dict], sample_ids: list[str]) -> dict:
    """Get formatted sample metrics."""
    formatted_sample_metrics: list = []
    for sample_id in sample_ids:
        collected_sample_metrics: dict = format_sample_metrics(
            collected_metrics=collected_metrics, sample_id=sample_id
        )
        formatted_sample_metrics.append(collected_sample_metrics)
    return {"samples": formatted_sample_metrics}


def get_case_metrics(collected_metrics: list[dict], case_id: str) -> dict:
    """Get case metrics."""
    case_metrics: list = []
    for metric in collected_metrics:
        for key in metric.keys():
            if key == case_id:
                case_metrics.append(metric)
    return {case_id: case_metrics}


def collect_balsamic_metrics(collect_qc_request: CollectQCRequest) -> Balsamic:
    """Collect multiqc metrics for balsamic workflow."""
    collected_metrics: list[dict] = collect_metrics(collect_qc_request)
    samples: dict = get_formatted_sample_metrics(
        collected_metrics=collected_metrics, sample_ids=collect_qc_request.sample_ids
    )
    case_metrics: dict = get_case_metrics(
        collected_metrics=collected_metrics, case_id=collect_qc_request.case_id
    )
    return Balsamic(
        case_id=collect_qc_request.case_id,
        samples=samples,
        somalier=case_metrics[FileTag.SOMALIER.value],
        workflow=collect_qc_request.workflow,
    )
