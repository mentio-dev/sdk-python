from enum import StrEnum


class GetUsageBreakdownBy(StrEnum):
    DAY = "day"
    GROUP = "group"
    KEYWORD = "keyword"
    PLATFORM = "platform"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
