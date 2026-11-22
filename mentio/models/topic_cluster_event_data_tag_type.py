from enum import StrEnum


class TopicClusterEventDataTagType(StrEnum):
    HASHTAG = "hashtag"
    INTENT = "intent"

    def __str__(self) -> str:
        return str(self.value)
