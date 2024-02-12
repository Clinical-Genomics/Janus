from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from janus.dto.post_request import CollectQCRequest

collect_qc_router = APIRouter()


@collect_qc_router.post(
    "/collect_qc/",
    response_description="Collect qc metrics for a case.",
)
def collect_qc(case: CollectQCRequest = Body(...),) -> JSONResponse:
    """Create a case document in the database."""
    pass