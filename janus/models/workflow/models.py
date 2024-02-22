"""Module for the workflow models."""
from pydantic import BaseModel

from janus.models.multiqc.models import (
    Somalier,
    PicardAlignmentSummary,
    PicardDups,
    PicardHsMetrics,
    PicardInsertSize,
    PicardWGSMetrics,
    SamtoolsStats,
    Fastp,
)


class BalsamicWGSSample(BaseModel):
    sample_id: str
    alignmentsummarymetrics: PicardAlignmentSummary | None
    dups: PicardDups | None
    wgsmetrics: PicardWGSMetrics | None
    hsmetrics: PicardHsMetrics | None
    insertsize: PicardInsertSize | None
    stats: SamtoolsStats
    fastp: Fastp


class BalsamicTGASample(BaseModel):
    sample_id: str
    alignmentsummarymetrics: PicardAlignmentSummary | None
    dups: PicardDups | None
    hsmetrics: PicardHsMetrics | None
    insertsize: PicardInsertSize | None
    stats: SamtoolsStats
    fastp: Fastp


class Balsamic(BaseModel):
    case_id: str
    samples: list[BalsamicWGSSample | BalsamicTGASample]
    somalier: Somalier
    workflow: str
