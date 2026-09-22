from enum import StrEnum


class ListViewsResponse200DataItemFilterNotSentimentsItem(StrEnum):
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"

    def __str__(self) -> str:
        return str(self.value)
