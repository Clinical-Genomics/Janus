"""Constants for the workflow sample models."""
from enum import Enum

from janus.models.workflow.models import BalsamicTGASample, BalsamicWGSSample


class WorkflowSampleModels(Enum):
    BALSAMIC_TGA: callable = BalsamicTGASample
    BALSAMIC_WGS: callable = BalsamicWGSSample
