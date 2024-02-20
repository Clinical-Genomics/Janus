"""Constants for the workflow sample models."""
from enum import Enum

from janus.models.multiqc.models import (
    PicardHsMetrics,
    PicardWGSMetrics,
    PeddyCheck,
    PicardDups,
    PicardInsertSize,
    Fastp,
    PicardAlignmentSummary,
    Somalier,
    PicardRNASeqMetrics,
    RNAfusionGeneralStats,
    STARAlignment,
)
from janus.models.workflow.models import BalsamicTGASample, BalsamicWGSSample


class MultiQCModels(Enum):
    PICARD_HS_METRICS: callable = PicardHsMetrics
    PICARD_WGS_METRICS: callable = PicardWGSMetrics
    PICARD_DUPS: callable = PicardDups
    PICARD_INSERT_SIZE: callable = PicardInsertSize
    PICARD_ALIGNMENT_SUMMARY: callable = PicardAlignmentSummary
    FASTP: callable = Fastp
    PEDDY_CHECK: callable = PeddyCheck
    SOMALIER: callable = Somalier
    PICARDRNASEQMETRICS: callable = PicardRNASeqMetrics
    STARALIGNMENT: callable = STARAlignment
    RNAFUSIONGENERALSTATS: callable = RNAfusionGeneralStats


class WorkflowSampleModels(Enum):
    BALSAMIC_TGA: callable = BalsamicTGASample
    BALSAMIC_WGS: callable = BalsamicWGSSample


class WorkflowParseFunctions(Enum):
    BALSAMIC_TGA: list[str] = [
        "SOMALIER",
        "FASTP",
        "PICARD_HS_METRICS",
        "PICARD_DUPS",
        "PICARD_INSERT_SIZE",
        "PICARD_ALIGNMENT_SUMMARY",
    ]
    BALSAMIC_WGS: list[str] = [
        "SOMALIER",
        "FASTP",
        "PICARD_HS_METRICS",
        "PICARD_DUPS",
        "PICARD_INSERT_SIZE",
        "PICARD_ALIGNMENT_SUMMARY",
        "PICARD_WGS_METRICS",
    ]
