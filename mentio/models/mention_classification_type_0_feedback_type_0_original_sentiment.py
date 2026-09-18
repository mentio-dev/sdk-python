from enum import StrEnum


class MentionClassificationType0FeedbackType0OriginalSentiment(StrEnum):
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"

    def __str__(self) -> str:
        return str(self.value)
