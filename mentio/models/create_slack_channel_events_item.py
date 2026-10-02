from enum import StrEnum


class CreateSlackChannelEventsItem(StrEnum):
    CHANNEL_FAILING = "channel.failing"
    KEYWORD_NOISY = "keyword.noisy"
    MENTION_SPIKE = "mention.spike"
    SENTIMENT_NEGATIVE_SPIKE = "sentiment.negative_spike"

    def __str__(self) -> str:
        return str(self.value)
