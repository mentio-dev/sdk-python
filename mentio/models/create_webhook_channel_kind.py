from enum import StrEnum


class CreateWebhookChannelKind(StrEnum):
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
