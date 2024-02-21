from enum import Enum

from janus.models.workflow.models import BalsamicTGASample, BalsamicWGSSample


class WorkflowToSampleModel(Enum):
    """Mapping for the workflow specific sample models."""

    BALSAMIC_TGA: callable = BalsamicTGASample
    BALSAMIC_WGS: callable = BalsamicWGSSample
