from enum import StrEnum


class ListAlertsResponse200DataItemMode(StrEnum):
    DAILY = "daily"
    INSTANT = "instant"

    def __str__(self) -> str:
        return str(self.value)
