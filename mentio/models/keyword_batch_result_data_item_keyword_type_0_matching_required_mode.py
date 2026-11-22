from enum import StrEnum


class KeywordBatchResultDataItemKeywordType0MatchingRequiredMode(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
