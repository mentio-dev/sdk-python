from enum import StrEnum


class CreateFeedBodyAuthType0Type(StrEnum):
    COOKIE = "cookie"

    def __str__(self) -> str:
        return str(self.value)
