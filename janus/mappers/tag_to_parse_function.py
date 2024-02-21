from enum import Enum

from janus.services.parser import parse_sample_metrics, parse_fastp, parse_somalier


class TagToParseFunction(Enum):
    hsmetrics: callable = parse_sample_metrics
    wgsmetrics: callable = parse_sample_metrics
    dups: callable = parse_sample_metrics
    insertsize: callable = parse_sample_metrics
    alignmentsummarymetrics: callable = parse_sample_metrics
    fastp: callable = parse_fastp
    peddycheck: callable = None
    somalier: callable = parse_somalier
    rnaseqmetrics: callable = None
    staralignment: callable = None
    rnafusiongeneralstats: callable = None
    stats: callable = parse_sample_metrics
