"""Module to hold the collect qc service."""

from janus.constants.FileTag import FileTag
from janus.constants.workflow import Workflow
from janus.dto.collect_qc_request import CollectQCRequest
from janus.dto.collect_qc_response import CollectQCResponse
from janus.exceptions.exceptions import WorkflowNotSupportedError
from janus.mappers.tag_to_parse_function import tag_to_parse_function
from janus.models.workflow.balsamic import Balsamic
from janus.services.workflow_collect_qc_services import WorkflowCollectQCService


class CollectQCService:
    def __init__(
        self, collect_qc_request: CollectQCRequest, collect_qc_service: WorkflowCollectQCService
    ):
        self.request: CollectQCRequest = collect_qc_request
        self.get_case_info: callable = collect_qc_service.get_case_info

    def collect_qc_metrics(self) -> CollectQCResponse:
        """Collect the qc metrics requested by the external source."""
        case_info: callable = self.get_case_info(self.request)
        qc_metrics = CollectQCResponse(case_id=self.request.case_id, case_info=case_info)
        return qc_metrics
