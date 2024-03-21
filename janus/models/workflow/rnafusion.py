"""Module for the RNAfusion workflow model."""

from pydantic import BaseModel, Field

from janus.constants.FileTag import FileTag
from janus.dto.collect_qc_request import WorkflowInfo
from janus.models.multiqc.models import (
    PicardDuplicates,
    PicardInsertSize,
    Fastp,
    STARAlignment,
    PicardRNASeqMetrics,
    RNAFusionGeneralStats,
)


class RNAFusionSample(BaseModel):
    duplicates: PicardDuplicates = Field(..., alias=FileTag.DUPLICATES)
    rna_seq_metrics: PicardRNASeqMetrics
    insert_size: PicardInsertSize = Field(..., alias=FileTag.INSERT_SIZE)
    star_alignment: STARAlignment
    fastp: Fastp = Field(..., alias=FileTag.FASTP)
    general_stats: RNAFusionGeneralStats


class RNAFusion(BaseModel):
    samples: list[RNAFusionSample]
    workflow: WorkflowInfo
