from enum import StrEnum


class ListAttentionStatus(StrEnum):
    ALL = "all"
    DISMISSED = "dismissed"
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
