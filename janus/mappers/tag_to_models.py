from enum import Enum

from janus.models.multiqc.models import (
    PicardHsMetrics,
    PicardWGSMetrics,
    PicardDups,
    PicardInsertSize,
    PicardAlignmentSummary,
    Fastp,
    PeddyCheck,
    Somalier,
    PicardRNASeqMetrics,
    STARAlignment,
    RNAfusionGeneralStats,
    SamtoolsStats,
)


class TagToModel(Enum):
    """Mapping for the multiqc models."""

    hsmetrics: callable = PicardHsMetrics
    wgsmetrics: callable = PicardWGSMetrics
    dups: callable = PicardDups
    insertsize: callable = PicardInsertSize
    alignmentsummarymetrics: callable = PicardAlignmentSummary
    fastp: callable = Fastp
    somalier: callable = Somalier
    stats: callable = SamtoolsStats
