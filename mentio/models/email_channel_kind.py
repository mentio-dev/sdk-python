from enum import StrEnum


class EmailChannelKind(StrEnum):
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
