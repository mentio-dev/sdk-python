from enum import StrEnum


class MentionStatus(StrEnum):
    DONE = "done"
    IGNORED = "ignored"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
