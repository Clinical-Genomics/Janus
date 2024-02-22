from fastapi import APIRouter, Body
from janus.dto.collect_qc_request import CollectQCRequest
from janus.dto.collect_qc_response import CollectQCResponse
from janus.services.collect_qc_service import CollectQCService
from pydantic import ValidationError

collect_qc_router = APIRouter()


@collect_qc_router.post(
    "/collect_qc/",
    response_description="Collect qc metrics for a case.",
    response_model=CollectQCResponse,
)
def collect_qc(collect_request: CollectQCRequest = Body(...)):
    """Collect qc metrics for the external request."""
    service = CollectQCService(collect_request)
    try:
        collected_qc_metrics = service.collect_qc_metrics_for_request()
        return CollectQCResponse(**collected_qc_metrics)
    except (ValueError, FileNotFoundError, ValidationError):
        pass
