from enum import StrEnum


class AlertMode(StrEnum):
    DAILY = "daily"
    INSTANT = "instant"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
