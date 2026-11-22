from enum import StrEnum


class UpdateKeywordBodySubredditKeep(StrEnum):
    ALL = "all"
    RELEVANT = "relevant"

    def __str__(self) -> str:
        return str(self.value)
