from enum import StrEnum


class UsageBreakdownBy(StrEnum):
    DAY = "day"
    KEYWORD = "keyword"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
