"""Balsamic Collect QC service."""

from janus.constants.FileTag import FileTag
from janus.dto.collect_qc_request import CollectQCRequest
from janus.models.workflow.balsamic import Balsamic
from janus.services.utils import get_formatted_sample_metrics, get_case_metrics, collect_metrics


class BalsamicCollectQCService:
    """Balsamic Collect QC service."""

    @staticmethod
    def extract_somalier(case_metrics: dict) -> dict:
        """Extract somalier metrics from case metrics."""
        for metric in case_metrics:
            somalier = metric[FileTag.SOMALIER]
            if not somalier:
                raise ValueError("No Somalier entry found.")
            return somalier

    def get_case_info(
        self,
        request: CollectQCRequest,
    ) -> Balsamic:
        """Collect multiqc metrics for balsamic workflow."""
        collected_metrics = collect_metrics(request)
        sample_metrics: list = get_formatted_sample_metrics(
            collected_metrics=collected_metrics, sample_ids=request.sample_ids
        )
        case_metrics: dict = get_case_metrics(
            collected_metrics=collected_metrics, case_id=request.case_id
        )
        somalier = self.extract_somalier(case_metrics[request.case_id])
        return Balsamic(
            samples=sample_metrics,
            somalier=somalier,
            workflow=request.workflow_info,
        )
