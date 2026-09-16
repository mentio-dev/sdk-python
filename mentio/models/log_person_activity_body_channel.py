from enum import StrEnum


class LogPersonActivityBodyChannel(StrEnum):
    BLUESKY = "bluesky"
    CALL = "call"
    EMAIL = "email"
    GITHUB = "github"
    LINKEDIN = "linkedin"
    MEETING = "meeting"
    OTHER = "other"
    REDDIT = "reddit"
    X = "x"

    def __str__(self) -> str:
        return str(self.value)
