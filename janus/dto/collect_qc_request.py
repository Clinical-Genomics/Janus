"""Post request model for JanusAPI."""

from pydantic import BaseModel


class CollectQCRequest(BaseModel):
    case_id: str
    sample_ids: list[str]
    file_names: list[str]
    workflow: str
    prep_category: str
