from enum import StrEnum


class AttentionItemSubjectType(StrEnum):
    CHANNEL = "channel"
    FEED = "feed"
    KEYWORD = "keyword"

    def __str__(self) -> str:
        return str(self.value)
