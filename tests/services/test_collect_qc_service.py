"""Tests for the collect qc service."""

from janus.dto.collect_qc_request import CollectQCRequest

from janus.dto.collect_qc_response import CollectQCResponse
from janus.models.multiqc.models import PicardWGSMetrics
from janus.services.collect_qc_service import CollectQCService


def test_collect_balsamic_metrics_wgs(
    collect_qc_service_balsamic_wgs: CollectQCService,
    collect_qc_request_balsamic_wgs: CollectQCRequest,
):
    # GIVEN a collect qc request for a balsamic workflow

    # WHEN collecting the qc metrics

    balsamic_metrics: CollectQCResponse = (
        collect_qc_service_balsamic_wgs.collect_qc_metrics(
            collect_qc_request_balsamic_wgs
        )
    )

    # THEN the metrics are returned
    assert isinstance(balsamic_metrics, CollectQCResponse)
    assert isinstance(
        balsamic_metrics.case_info.samples[0].wgs_metrics, PicardWGSMetrics
    )


def test_collect_balsamic_metrics_tga(
    collect_qc_service_balsamic_tga: CollectQCService,
    collect_qc_request_balsamic_tga: CollectQCRequest,
):
    # GIVEN a collect qc request for a balsamic workflow

    # WHEN collecting the qc metrics

    balsamic_metrics: CollectQCResponse = (
        collect_qc_service_balsamic_tga.collect_qc_metrics(
            collect_qc_request_balsamic_tga
        )
    )

    # THEN the metrics are returned
    assert isinstance(balsamic_metrics, CollectQCResponse)
    assert not balsamic_metrics.case_info.samples[0].wgs_metrics
