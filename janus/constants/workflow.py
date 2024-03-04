"""Constant for the workflows."""

from enum import StrEnum


class Workflow(StrEnum):
    BALSAMIC: str = "balsamic"
    BALSAMIC_QC: str = "balsamic-qc"
    BALSAMIC_UMI: str = "balsamic-umi"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
