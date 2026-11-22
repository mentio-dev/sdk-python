from enum import StrEnum


class CreateExportBodyFilterStatus(StrEnum):
    DONE = "done"
    IGNORED = "ignored"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
