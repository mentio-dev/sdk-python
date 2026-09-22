from enum import StrEnum


class ListViewsResponse200DataItemFilterSentimentsItem(StrEnum):
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"

    def __str__(self) -> str:
        return str(self.value)
