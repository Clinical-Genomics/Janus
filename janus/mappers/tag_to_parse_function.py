from janus.constants.FileTag import FileTag
from janus.services.parser import (
    parse_fastp,
    parse_general_stats,
    parse_sample_metrics,
    parse_somalier,
)

tag_to_parse_function: dict = {
    FileTag.ALIGNMENT_SUMMARY_METRICS: parse_sample_metrics,
    FileTag.DUPLICATES: parse_sample_metrics,
    FileTag.FASTP: parse_fastp,
    FileTag.GENERAL_STATS: parse_general_stats,
    FileTag.HS_METRICS: parse_sample_metrics,
    FileTag.INSERT_SIZE: parse_sample_metrics,
    FileTag.RNA_SEQ_METRICS: parse_sample_metrics,
    FileTag.SAMTOOLS_STATS: parse_sample_metrics,
    FileTag.SOMALIER: parse_somalier,
    FileTag.STAR: parse_sample_metrics,
    FileTag.WGS_METRICS: parse_sample_metrics,
}
