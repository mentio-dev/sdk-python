from enum import StrEnum


class GetAnalyticsSeriesBy(StrEnum):
    KEYWORD = "keyword"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
