from enum import StrEnum


class TelegramChannelConfigChatType(StrEnum):
    CHANNEL = "channel"
    GROUP = "group"
    PRIVATE = "private"
    SUPERGROUP = "supergroup"

    def __str__(self) -> str:
        return str(self.value)
