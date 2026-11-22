from enum import StrEnum


class UpdateExportScheduleBodyWeekday(StrEnum):
    FRIDAY = "friday"
    MONDAY = "monday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    THURSDAY = "thursday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"

    def __str__(self) -> str:
        return str(self.value)
