from enum import StrEnum


class FeedAuthType0Type(StrEnum):
    COOKIE = "cookie"
    HEADER = "header"

    def __str__(self) -> str:
        return str(self.value)
