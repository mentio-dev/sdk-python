from enum import StrEnum


class CreateWebhookChannelEventsItem(StrEnum):
    ACCOUNT_CAPPED = "account.capped"
    ACCOUNT_PAUSED = "account.paused"
    ACCOUNT_RESUMED = "account.resumed"
    CHANNEL_FAILING = "channel.failing"
    EXPORT_READY = "export.ready"
    FEED_FAILING = "feed.failing"
    FEED_RECOVERED = "feed.recovered"
    FOLLOWERS_NEW = "followers.new"
    KEYWORD_CAPPED = "keyword.capped"
    KEYWORD_NOISY = "keyword.noisy"
    KEYWORD_PAUSED_FOR_BALANCE = "keyword.paused_for_balance"
    KEYWORD_RESUMED = "keyword.resumed"
    MENTION_SPIKE = "mention.spike"
    MENTION_TOPIC_CLUSTER = "mention.topic_cluster"
    MENTION_UNANSWERED_INFLUENCER = "mention.unanswered_influencer"
    SENTIMENT_NEGATIVE_SPIKE = "sentiment.negative_spike"
    WALLET_LOW = "wallet.low"
    WALLET_PAUSED = "wallet.paused"
    WALLET_RESUMED = "wallet.resumed"

    def __str__(self) -> str:
        return str(self.value)
