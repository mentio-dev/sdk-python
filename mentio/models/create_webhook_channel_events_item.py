from enum import StrEnum


class CreateWebhookChannelEventsItem(StrEnum):
    KEYWORD_CAPPED = "keyword.capped"
    KEYWORD_PAUSED_FOR_BALANCE = "keyword.paused_for_balance"
    KEYWORD_RESUMED = "keyword.resumed"
    WALLET_LOW = "wallet.low"
    WALLET_PAUSED = "wallet.paused"
    WALLET_RESUMED = "wallet.resumed"

    def __str__(self) -> str:
        return str(self.value)
