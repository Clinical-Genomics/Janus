from pydantic import BaseModel

from janus.models.workflow.models import BalsamicTGASample, BalsamicWGSSample, Balsamic


class CollectQCResponse(BaseModel):
    """Collect QC response model."""

    case_id: str
    case_info: Balsamic
