from enum import StrEnum


class CreateExportScheduleBodyCadence(StrEnum):
    DAILY = "daily"
    HOURLY = "hourly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
