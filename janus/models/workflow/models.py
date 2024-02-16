"""Module for the workflow models."""
from pydantic import BaseModel

from janus.models.multiqc.models import (
    Somalier,
    PicardAlignmentSummary,
    PicardDups,
    PicardHsMetrics,
    PicardInsertSize,
    PicardWGSMetrics,
)


class BalsamicWGSSample(BaseModel):
    sample_id: str
    picard_alignment_summary: PicardAlignmentSummary | None
    picard_dups: PicardDups | None
    picard_wgs_metrics: PicardWGSMetrics | None
    picard_hs_metrics: PicardHsMetrics | None
    picard_insert_size: PicardInsertSize | None
    somalier: Somalier | None


class BalsamicTGASample(BaseModel):
    sample_id: str
    picard_alignment_summary: PicardAlignmentSummary | None
    picard_dups: PicardDups | None
    picard_hs_metrics: PicardHsMetrics | None
    picard_insert_size: PicardInsertSize | None
    somalier: Somalier | None
