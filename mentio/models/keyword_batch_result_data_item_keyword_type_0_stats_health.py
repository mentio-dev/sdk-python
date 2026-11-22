from enum import StrEnum


class KeywordBatchResultDataItemKeywordType0StatsHealth(StrEnum):
    CAPPED = "capped"
    HEALTHY = "healthy"
    NEW = "new"
    NOISY = "noisy"
    PAUSED = "paused"
    QUIET = "quiet"

    def __str__(self) -> str:
        return str(self.value)
