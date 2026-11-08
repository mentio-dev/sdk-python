from enum import StrEnum


class ListKeywordsNotStatusesItem(StrEnum):
    ACTIVE = "active"
    CAPPED = "capped"
    MUTED = "muted"
    NOISY = "noisy"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
