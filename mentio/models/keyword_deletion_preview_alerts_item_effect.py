from enum import StrEnum


class KeywordDeletionPreviewAlertsItemEffect(StrEnum):
    DISABLED = "disabled"
    EMPTY = "empty"
    NARROWED = "narrowed"

    def __str__(self) -> str:
        return str(self.value)
