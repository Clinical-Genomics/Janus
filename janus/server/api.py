from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from janus.dto.collect_qc_request import CollectQCRequest
from janus.dto.collect_qc_response import CollectQCResponse

collect_qc_router = APIRouter()


@collect_qc_router.get(
    "/collect_qc/",
    response_description="Collect qc metrics for a case.",
    response_model=CollectQCResponse,
)
def collect_qc(collect_request: CollectQCRequest = Body(...)) -> JSONResponse:
    """Create a case document in the database."""
    pass
