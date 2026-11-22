from enum import StrEnum


class CreateExportScheduleBodyFormat(StrEnum):
    CSV = "csv"
    JSONL = "jsonl"

    def __str__(self) -> str:
        return str(self.value)
