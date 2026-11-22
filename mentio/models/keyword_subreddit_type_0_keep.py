from enum import StrEnum


class KeywordSubredditType0Keep(StrEnum):
    ALL = "all"
    RELEVANT = "relevant"

    def __str__(self) -> str:
        return str(self.value)
