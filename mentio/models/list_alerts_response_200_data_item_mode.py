from enum import StrEnum


class ListAlertsResponse200DataItemMode(StrEnum):
    DAILY = "daily"
    HOURLY = "hourly"
    INSTANT = "instant"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
