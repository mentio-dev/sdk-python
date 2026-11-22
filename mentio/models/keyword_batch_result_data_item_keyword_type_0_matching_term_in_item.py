from enum import StrEnum


class KeywordBatchResultDataItemKeywordType0MatchingTermInItem(StrEnum):
    AUTHOR = "author"
    BODY = "body"
    TITLE = "title"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
