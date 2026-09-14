from enum import StrEnum


class ListAlertsResponse200DataItemChannelsItemKind(StrEnum):
    EMAIL = "email"
    SLACK = "slack"
    TELEGRAM = "telegram"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
