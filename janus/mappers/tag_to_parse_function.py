from janus.constants.FileTag import FileTag
from janus.services.parser import parse_sample_metrics, parse_fastp, parse_somalier

tag_to_parse_function: dict = {
    FileTag.HS_METRICS: parse_sample_metrics,
    FileTag.WGS_METRICS: parse_sample_metrics,
    FileTag.DUPS: parse_sample_metrics,
    FileTag.INSERT_SIZE: parse_sample_metrics,
    FileTag.ALIGNMENT_SUMMARY_METRICS: parse_sample_metrics,
    FileTag.FASTP: parse_fastp,
    FileTag.PEDDY_CHECK: parse_sample_metrics,
    FileTag.SOMALIER: parse_somalier,
    FileTag.RNASEQ_METRICS: parse_sample_metrics,
    FileTag.STAR_ALIGNMENT: parse_sample_metrics,
    FileTag.RNAFUSION_GENERAL_STATS: parse_sample_metrics,
    FileTag.STATS: parse_sample_metrics,
}
