from enum import StrEnum


class ListKeywordsStatusItem(StrEnum):
    ACTIVE = "active"
    MUTED = "muted"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
