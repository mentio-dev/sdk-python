from enum import StrEnum


class DiscordChannelKind(StrEnum):
    DISCORD = "discord"

    def __str__(self) -> str:
        return str(self.value)
