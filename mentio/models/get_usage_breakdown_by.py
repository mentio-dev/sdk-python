from enum import StrEnum


class GetUsageBreakdownBy(StrEnum):
    DAY = "day"
    KEYWORD = "keyword"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
