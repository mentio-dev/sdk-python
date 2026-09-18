from enum import StrEnum


class ListKeywordsResponse200DataItemMatchingRequiredMode(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
