from enum import StrEnum


class ListKeywordsSort(StrEnum):
    LASTMENTION = "lastMention"
    MENTIONS = "mentions"
    NEWEST = "newest"
    OLDEST = "oldest"
    RECENT = "recent"
    RELEVANT = "relevant"
    TERM = "term"

    def __str__(self) -> str:
        return str(self.value)
