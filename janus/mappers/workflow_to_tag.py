from enum import Enum


class WorkflowToTag(Enum):
    """Mapping for the models that are required to be parsed for each workflow."""

    BALSAMIC_TGA: list[str] = [
        "somalier",
        "fastp",
        "hsmetrics",
        "dups",
        "insertsize",
        "alignmentsummarymetrics",
        "stats",
    ]
    BALSAMIC_WGS: list[str] = [
        "somalier",
        "fastp",
        "hsmetrics",
        "dups",
        "insertsize",
        "alignmentsummarymetrics",
        "wgsmetrics",
        "stats",
    ]
