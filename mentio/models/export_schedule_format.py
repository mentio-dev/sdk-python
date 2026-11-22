from enum import StrEnum


class ExportScheduleFormat(StrEnum):
    CSV = "csv"
    JSONL = "jsonl"

    def __str__(self) -> str:
        return str(self.value)
