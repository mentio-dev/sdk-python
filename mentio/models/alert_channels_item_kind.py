from enum import StrEnum


class AlertChannelsItemKind(StrEnum):
    DISCORD = "discord"
    EMAIL = "email"
    SLACK = "slack"
    TEAMS = "teams"
    TELEGRAM = "telegram"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
