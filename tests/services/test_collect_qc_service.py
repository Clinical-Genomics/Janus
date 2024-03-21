"""Tests for the collect qc service."""

import pytest

from janus.dto.collect_qc_response import CollectQCResponse
from janus.exceptions.exceptions import WorkflowNotSupportedError
from janus.models.multiqc.models import PicardWGSMetrics
from janus.services.collect_qc_service import CollectQCService


def test_collect_metrics_for_models(collect_balsamic_qc_service_wgs: CollectQCService):
    # GIVEN a collect qc request
    expected_keys: list[str] = [
        collect_balsamic_qc_service_wgs.request.sample_ids[0],
        collect_balsamic_qc_service_wgs.request.sample_ids[1],
        collect_balsamic_qc_service_wgs.request.case_id,
    ]

    # WHEN collecting the metrics for the models
    collected_metrics: list[dict] = collect_balsamic_qc_service_wgs.collect_metrics()

    # THEN the metrics are returned
    for metric in collected_metrics:
        for key, value in metric.items():
            assert key in expected_keys


def test_collect_balsamic_metrics_wgs(
    collect_balsamic_qc_service_wgs: CollectQCService,
):
    # GIVEN a collect qc request for a balsamic workflow

    # WHEN collecting the qc metrics
    balsamic_metrics: CollectQCResponse = (
        collect_balsamic_qc_service_wgs.collect_qc_metrics_for_request()
    )

    # THEN the metrics are returned
    assert isinstance(balsamic_metrics, CollectQCResponse)
    assert isinstance(balsamic_metrics.case_info.samples[0].wgs_metrics, PicardWGSMetrics)


def test_collect_balsamic_metrics_tga(
    collect_balsamic_qc_service_tga: CollectQCService,
):
    # GIVEN a collect qc request for a balsamic workflow

    # WHEN collecting the qc metrics
    balsamic_metrics: CollectQCResponse = (
        collect_balsamic_qc_service_tga.collect_qc_metrics_for_request()
    )

    # THEN the metrics are returned
    assert isinstance(balsamic_metrics, CollectQCResponse)
    assert not balsamic_metrics.case_info.samples[0].wgs_metrics


def test_collect_unsupported_metrics(
    collect_qc_service_unsupported_workflow: CollectQCService,
):
    # GIVEN a collect qc request for an unsupported workflow

    # WHEN collecting the qc metrics

    # THEN an error is raised
    with pytest.raises(WorkflowNotSupportedError):
        collect_qc_service_unsupported_workflow.collect_qc_metrics_for_request()
