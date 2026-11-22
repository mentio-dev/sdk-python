from enum import StrEnum


class ExportScheduleDestinationType0Kind(StrEnum):
    LINK = "link"

    def __str__(self) -> str:
        return str(self.value)
