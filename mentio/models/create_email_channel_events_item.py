from enum import StrEnum


class CreateEmailChannelEventsItem(StrEnum):
    CHANNEL_FAILING = "channel.failing"
    FEED_FAILING = "feed.failing"
    FEED_RECOVERED = "feed.recovered"
    KEYWORD_NOISY = "keyword.noisy"
    MENTION_SPIKE = "mention.spike"
    MENTION_TOPIC_CLUSTER = "mention.topic_cluster"
    MENTION_UNANSWERED_INFLUENCER = "mention.unanswered_influencer"
    SENTIMENT_NEGATIVE_SPIKE = "sentiment.negative_spike"

    def __str__(self) -> str:
        return str(self.value)
