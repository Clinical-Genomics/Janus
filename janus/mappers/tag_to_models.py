from janus.constants.FileTag import FileTag
from janus.models.multiqc.models import (
    Fastp,
    PicardAlignmentSummary,
    PicardDuplicates,
    PicardHsMetrics,
    PicardInsertSize,
    PicardRNASeqMetrics,
    PicardWGSMetrics,
    RNAFusionGeneralStats,
    SamtoolsStats,
    Somalier,
)

tag_to_model = {
    FileTag.ALIGNMENT_SUMMARY_METRICS: PicardAlignmentSummary,
    FileTag.DUPLICATES: PicardDuplicates,
    FileTag.FASTP: Fastp,
    FileTag.GENERAL_STATS: RNAFusionGeneralStats,
    FileTag.HS_METRICS: PicardHsMetrics,
    FileTag.INSERT_SIZE: PicardInsertSize,
    FileTag.RNA_SEQ_METRICS: PicardRNASeqMetrics,
    FileTag.SAMTOOLS_STATS: SamtoolsStats,
    FileTag.SOMALIER: Somalier,
    FileTag.WGS_METRICS: PicardWGSMetrics,
}
