from enum import StrEnum


class CreateDiscordChannelKind(StrEnum):
    DISCORD = "discord"

    def __str__(self) -> str:
        return str(self.value)
