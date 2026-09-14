from enum import StrEnum


class UpdateAlertBodyMode(StrEnum):
    DAILY = "daily"
    INSTANT = "instant"

    def __str__(self) -> str:
        return str(self.value)
