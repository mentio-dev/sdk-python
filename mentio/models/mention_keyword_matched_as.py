from enum import StrEnum


class MentionKeywordMatchedAs(StrEnum):
    CLOSE_WORDS = "close_words"
    PHRASE = "phrase"
    SUBREDDIT = "subreddit"

    def __str__(self) -> str:
        return str(self.value)
