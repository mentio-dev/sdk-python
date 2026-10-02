from enum import StrEnum


class AttentionItemStatus(StrEnum):
    DISMISSED = "dismissed"
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
