from enum import StrEnum


class AlertChannelsItemKind(StrEnum):
    EMAIL = "email"
    SLACK = "slack"
    TELEGRAM = "telegram"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
