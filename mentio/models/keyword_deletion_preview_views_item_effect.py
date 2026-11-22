from enum import StrEnum


class KeywordDeletionPreviewViewsItemEffect(StrEnum):
    DISABLED = "disabled"
    EMPTY = "empty"
    NARROWED = "narrowed"

    def __str__(self) -> str:
        return str(self.value)
