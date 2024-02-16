from pydantic import BaseModel

from janus.models.workflow.models import BalsamicTGASample, BalsamicWGSSample


class CollectQCResponse(BaseModel):
    """Collect QC response model."""

    case_id: str
    samples: list[BalsamicWGSSample | BalsamicTGASample]
