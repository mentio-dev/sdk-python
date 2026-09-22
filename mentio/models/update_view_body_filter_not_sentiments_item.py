from enum import StrEnum


class UpdateViewBodyFilterNotSentimentsItem(StrEnum):
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"

    def __str__(self) -> str:
        return str(self.value)
