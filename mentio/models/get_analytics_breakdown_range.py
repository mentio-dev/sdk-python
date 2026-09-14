from enum import StrEnum


class GetAnalyticsBreakdownRange(StrEnum):
    VALUE_0 = "7d"
    VALUE_1 = "30d"
    VALUE_2 = "90d"
    VALUE_3 = "365d"

    def __str__(self) -> str:
        return str(self.value)
