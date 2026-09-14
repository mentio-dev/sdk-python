from enum import StrEnum


class CreateEmailChannelKind(StrEnum):
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
