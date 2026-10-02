from enum import StrEnum


class CreateWebhookChannelEventsItem(StrEnum):
    CHANNEL_FAILING = "channel.failing"
    KEYWORD_CAPPED = "keyword.capped"
    KEYWORD_NOISY = "keyword.noisy"
    KEYWORD_PAUSED_FOR_BALANCE = "keyword.paused_for_balance"
    KEYWORD_RESUMED = "keyword.resumed"
    MENTION_SPIKE = "mention.spike"
    SENTIMENT_NEGATIVE_SPIKE = "sentiment.negative_spike"
    WALLET_LOW = "wallet.low"
    WALLET_PAUSED = "wallet.paused"
    WALLET_RESUMED = "wallet.resumed"

    def __str__(self) -> str:
        return str(self.value)
