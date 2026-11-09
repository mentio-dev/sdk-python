from enum import StrEnum


class AutomationFilterNotSentimentsItem(StrEnum):
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"

    def __str__(self) -> str:
        return str(self.value)
