from enum import StrEnum


class KeywordEstimateStatus(StrEnum):
    DONE = "done"
    FAILED = "failed"
    QUEUED = "queued"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
