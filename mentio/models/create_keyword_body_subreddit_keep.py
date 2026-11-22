from enum import StrEnum


class CreateKeywordBodySubredditKeep(StrEnum):
    ALL = "all"
    RELEVANT = "relevant"

    def __str__(self) -> str:
        return str(self.value)
