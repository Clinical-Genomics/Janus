"Module to map the workflows to the services."

from janus.constants.workflow import Workflow
from janus.services.balsamic_collect_qc_service import BalsamicCollectQCService


workflow_to_service = {
    Workflow.BALSAMIC: BalsamicCollectQCService(),
    Workflow.BALSAMIC_QC: BalsamicCollectQCService(),
    Workflow.BALSAMIC_UMI: BalsamicCollectQCService(),
}
