from enum import StrEnum


class ListAlertsResponse200DataItemChannelsItemKind(StrEnum):
    DISCORD = "discord"
    EMAIL = "email"
    SLACK = "slack"
    TEAMS = "teams"
    TELEGRAM = "telegram"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
