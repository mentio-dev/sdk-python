from enum import StrEnum


class AnalyticsSeriesWindowBucket(StrEnum):
    DAY = "day"
    HOUR = "hour"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
