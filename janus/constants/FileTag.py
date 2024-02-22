from enum import StrEnum


class FileTag(StrEnum):
    """File tags."""

    HS_METRICS: str = "hsmetrics"
    WGS_METRICS: str = "wgsmetrics"
    DUPS: str = "dups"
    INSERT_SIZE: str = "insertsize"
    ALIGNMENT_SUMMARY_METRICS: str = "alignmentsummarymetrics"
    FASTP: str = "fastp"
    PEDDY_CHECK: str = "peddycheck"
    SOMALIER: str = "somalier"
    RNASEQ_METRICS: str = "rnaseqmetrics"
    STAR_ALIGNMENT: str = "staralignment"
    RNAFUSION_GENERAL_STATS: str = "rnafusiongeneralstats"
    STATS: str = "stats"
