from enum import StrEnum


class RunAlertDigestResponse200Skipped(StrEnum):
    ALREADY_SENT = "already_sent"
    EMPTY = "empty"

    def __str__(self) -> str:
        return str(self.value)
