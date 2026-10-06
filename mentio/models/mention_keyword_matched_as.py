from enum import StrEnum


class MentionKeywordMatchedAs(StrEnum):
    CLOSE_WORDS = "close_words"
    PHRASE = "phrase"

    def __str__(self) -> str:
        return str(self.value)
