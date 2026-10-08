from enum import StrEnum


class DuplicateKeywordBodyIncludeItem(StrEnum):
    FEEDS = "feeds"
    REVIEWSOURCES = "reviewSources"

    def __str__(self) -> str:
        return str(self.value)
