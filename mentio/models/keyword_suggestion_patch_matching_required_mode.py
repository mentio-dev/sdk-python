from enum import StrEnum


class KeywordSuggestionPatchMatchingRequiredMode(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
