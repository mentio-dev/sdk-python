from enum import StrEnum


class ImportFeedsResponse200DataItemFeedType0AuthType0Type(StrEnum):
    COOKIE = "cookie"
    HEADER = "header"

    def __str__(self) -> str:
        return str(self.value)
