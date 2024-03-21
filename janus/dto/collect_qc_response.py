from janus.models.workflow.balsamic import Balsamic
from janus.models.workflow.rnafusion import RNAFusion
from pydantic import BaseModel


class CollectQCResponse(BaseModel):
    """Collect QC response model."""

    case_id: str
    case_info: Balsamic | RNAFusion
