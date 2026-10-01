from enum import StrEnum


class KeywordSuggestionSource(StrEnum):
    AI = "ai"
    RULES = "rules"

    def __str__(self) -> str:
        return str(self.value)
