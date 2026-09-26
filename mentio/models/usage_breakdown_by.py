from enum import StrEnum


class UsageBreakdownBy(StrEnum):
    DAY = "day"
    GROUP = "group"
    KEYWORD = "keyword"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
