from enum import StrEnum


class GetAnalyticsBreakdownBy(StrEnum):
    HOUR = "hour"
    INTENT = "intent"
    KEYWORD = "keyword"
    PERSON = "person"
    PLATFORM = "platform"
    SENTIMENT = "sentiment"
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
