from enum import StrEnum


class AnalyticsBreakdownBy(StrEnum):
    COUNTRY = "country"
    HOUR = "hour"
    INTENT = "intent"
    KEYWORD = "keyword"
    LANGUAGE = "language"
    PERSON = "person"
    PLATFORM = "platform"
    SENTIMENT = "sentiment"
    STATUS = "status"
    SUBREDDIT = "subreddit"

    def __str__(self) -> str:
        return str(self.value)
