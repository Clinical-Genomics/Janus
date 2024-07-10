"""Balsamic Collect QC service."""

from abc import ABC

from janus.constants.FileTag import FileTag
from janus.dto.collect_qc_request import CollectQCRequest
from janus.models.workflow.balsamic import Balsamic
from janus.services.utils import get_formatted_sample_metrics, get_case_metrics, collect_metrics


class WorkflowCollectQCService(ABC):
    """Abstract class for workflow collect qc service."""

    def get_case_info(self, request: CollectQCRequest) -> None:
        """Get the case info."""
        pass


class BalsamicCollectQCService(WorkflowCollectQCService):
    """Balsamic Collect QC service."""

    @staticmethod
    def extract_somalier_metrics(case_metrics: dict) -> dict:
        """Extract Somalier metrics from case metrics."""
        for metric in case_metrics:
            somalier_metrics: dict = metric[FileTag.SOMALIER]
            if not somalier_metrics:
                raise ValueError("No Somalier entry found.")
            return somalier_metrics

    def get_case_info(
        self,
        request: CollectQCRequest,
    ) -> Balsamic:
        """Collect MultiQC metrics for Balsamic workflow."""
        collected_metrics: list[dict] = collect_metrics(request)
        sample_metrics: list = get_formatted_sample_metrics(
            collected_metrics=collected_metrics, sample_ids=request.sample_ids
        )
        case_metrics: dict = get_case_metrics(
            collected_metrics=collected_metrics, case_id=request.case_id
        )
        somalier_metrics: dict = self.extract_somalier_metrics(case_metrics[request.case_id])
        return Balsamic(
            samples=sample_metrics,
            somalier=somalier_metrics,
            workflow=request.workflow_info,
        )
