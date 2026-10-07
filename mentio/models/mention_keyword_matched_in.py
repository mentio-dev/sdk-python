from enum import StrEnum


class MentionKeywordMatchedIn(StrEnum):
    SPEECH = "speech"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
