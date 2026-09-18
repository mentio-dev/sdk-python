from enum import StrEnum


class CreateAlertBodyMode(StrEnum):
    DAILY = "daily"
    INSTANT = "instant"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
