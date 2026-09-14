from enum import StrEnum


class TelegramChannelKind(StrEnum):
    TELEGRAM = "telegram"

    def __str__(self) -> str:
        return str(self.value)
