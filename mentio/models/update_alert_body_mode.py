from enum import StrEnum


class UpdateAlertBodyMode(StrEnum):
    DAILY = "daily"
    HOURLY = "hourly"
    INSTANT = "instant"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
