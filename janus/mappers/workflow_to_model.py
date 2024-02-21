from enum import Enum

from janus.models.workflow.models import Balsamic


class WorkflowToModel(Enum):
    """Mapping for the models that are required to be parsed for each workflow."""

    balsamic: Balsamic

