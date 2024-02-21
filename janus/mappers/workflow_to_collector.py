"""Maps the workflows to their collector functions."""
from janus.services.collect_qc_service import collect_balsamic_metrics

workflow_to_collector = {"blasamic": collect_balsamic_metrics}
