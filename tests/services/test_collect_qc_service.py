"""Tests for the collect qc service."""
from janus.dto.collect_qc_request import CollectQCRequest
from janus.models.workflow.models import BalsamicWGSSample, BalsamicTGASample
from janus.services.collect_qc_service import (
    get_sample_model,
    add_sample_id_to_model,
    prepare_sample_models,
    collect_metrics_for_models,
)


def test_get_sample_model(balsamic_workflow: str, wgs_prep_category: str):

    # GIVEN a workflow and a prep category

    # WHEN retrieving the sample model
    sample_model: BalsamicWGSSample = get_sample_model(
        workflow=balsamic_workflow, prep_category=wgs_prep_category
    )

    # THEN the sample model is returned
    isinstance(sample_model, BalsamicWGSSample)


def test_add_sample_id_to_model(sample_ids: list[str] = ["sample_a", "sample_b"]):

    # GIVEN a list of sample ids and a sample model

    # WHEN adding the sample ids to the sample model
    modified_models: list[BalsamicWGSSample] = add_sample_id_to_model(
        sample_ids=sample_ids, sample_model=BalsamicWGSSample
    )

    # THEN a list of sample models with sample ids is returned
    for modified_model in modified_models:
        assert isinstance(modified_model, type(BalsamicTGASample))
        assert modified_model.sample_id in sample_ids


def test_prepare_sample_models(collect_qc_request: CollectQCRequest):

    # GIVEN a collect qc request

    # WHEN preparing the sample models
    prepared_models: list[BalsamicTGASample] = prepare_sample_models(collect_qc_request)

    # THEN the sample models are prepared
    for model in prepared_models:
        assert isinstance(model, type(BalsamicTGASample))
        assert model.sample_id in collect_qc_request.sample_ids


def test_collect_metrics_for_models(collect_qc_request_balsamic_wgs):

    # GIVEN a collect qc request
    expected_keys: list[str] = [collect_qc_request_balsamic_wgs.sample_ids[0],
                                collect_qc_request_balsamic_wgs.sample_ids[1],
                                collect_qc_request_balsamic_wgs.case_id
                                ]
    # WHEN collecting the metrics for the models
    collected_metrics: list[dict] = collect_metrics_for_models(
        collect_qc_request_balsamic_wgs,
    )

    # THEN the metrics are returned
    for metric in collected_metrics:
        for key, value in metric.items():
            assert key in expected_keys
