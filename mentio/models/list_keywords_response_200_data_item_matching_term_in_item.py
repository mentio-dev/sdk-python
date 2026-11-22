from enum import StrEnum


class ListKeywordsResponse200DataItemMatchingTermInItem(StrEnum):
    AUTHOR = "author"
    BODY = "body"
    TITLE = "title"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
