from enum import StrEnum


class ListFeedsResponse200DataItemAuthType0Type(StrEnum):
    COOKIE = "cookie"
    HEADER = "header"

    def __str__(self) -> str:
        return str(self.value)
