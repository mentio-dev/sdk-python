from enum import StrEnum


class AnalyticsSeriesPreviousType0ItemKeywordType0Kind(StrEnum):
    BRAND = "brand"
    COMPETITOR = "competitor"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
