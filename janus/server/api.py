from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from janus.dto.collect_qc_request import CollectQCRequest
from janus.dto.collect_qc_response import CollectQCResponse
from janus.mappers.workflow_to_collector import workflow_to_collector
from janus.models.workflow.models import Balsamic
from janus.services.collect_qc_service import CollectQCService

collect_qc_router = APIRouter()


@collect_qc_router.get(
    "/collect_qc/",
    response_description="Collect qc metrics for a case.",
    response_model=CollectQCResponse,
)
def collect_qc(collect_request: CollectQCRequest = Body(...)):
    """Create a case document in the database."""
    service = CollectQCService(collect_request)
    collected_qc_metrics = service.collect_qc_metrics_for_request()
    return CollectQCResponse(**collected_qc_metrics)
