from enum import StrEnum


class ChannelFailingEventDataChannelKind(StrEnum):
    EMAIL = "email"
    SLACK = "slack"
    TELEGRAM = "telegram"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
