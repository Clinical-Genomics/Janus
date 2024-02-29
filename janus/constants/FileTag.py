from enum import StrEnum


class FileTag(StrEnum):
    """File tags."""

    HS_METRICS: str = "picard-hs"
    WGS_METRICS: str = "picard-wgs"
    DUPLICATES: str = "picard-duplicates"
    INSERT_SIZE: str = "picard-insert-size"
    ALIGNMENT_SUMMARY_METRICS: str = "picard-alignment"
    FASTP: str = "fastp"
    PEDDY_CHECK: str = ""
    SOMALIER: str = "somalier"
    RNASEQ_METRICS: str = ""
    STAR_ALIGNMENT: str = "star"
    RNAFUSION_GENERAL_STATS: str = ""
    SAMTOOLS_STATS: str = "samtools-stats"
