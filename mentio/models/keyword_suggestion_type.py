from enum import StrEnum


class KeywordSuggestionType(StrEnum):
    CONTEXT = "context"
    EXCLUDED_AUTHORS = "excluded_authors"
    EXCLUDED_TERMS = "excluded_terms"
    PLATFORMS = "platforms"
    REQUIRED_TERMS = "required_terms"

    def __str__(self) -> str:
        return str(self.value)
