from enum import StrEnum


class GetAnalyticsBreakdownBy(StrEnum):
    COUNTRY = "country"
    DOMAIN = "domain"
    EMOTION = "emotion"
    HASHTAG = "hashtag"
    HOUR = "hour"
    INTENT = "intent"
    KEYWORD = "keyword"
    LANGUAGE = "language"
    LINK = "link"
    PERSON = "person"
    PLATFORM = "platform"
    SENTIMENT = "sentiment"
    STATUS = "status"
    SUBREDDIT = "subreddit"

    def __str__(self) -> str:
        return str(self.value)
