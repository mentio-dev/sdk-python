from enum import StrEnum


class KeywordDeletionPreviewAutomationsItemEffect(StrEnum):
    DISABLED = "disabled"
    EMPTY = "empty"
    NARROWED = "narrowed"

    def __str__(self) -> str:
        return str(self.value)
