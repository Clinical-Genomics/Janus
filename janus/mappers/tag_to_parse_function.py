from janus.constants.FileTag import FileTag
from janus.services.parser import parse_sample_metrics, parse_fastp, parse_somalier

tag_to_parse_function: dict = {
    FileTag.HS_METRICS.value: parse_sample_metrics,
    FileTag.WGS_METRICS.value : parse_sample_metrics,
    FileTag.DUPS.value : parse_sample_metrics,
    FileTag.INSERT_SIZE.value : parse_sample_metrics,
    FileTag.ALIGNMENT_SUMMARY_METRICS.value : parse_sample_metrics,
    FileTag.FASTP.value : parse_fastp,
    FileTag.PEDDY_CHECK.value : parse_sample_metrics,
    FileTag.SOMALIER.value : parse_somalier,
    FileTag.RNASEQ_METRICS.value : parse_sample_metrics,
    FileTag.STAR_ALIGNMENT.value : parse_sample_metrics,
    FileTag.RNAFUSION_GENERAL_STATS.value : parse_sample_metrics,
    FileTag.STATS.value : parse_sample_metrics
}