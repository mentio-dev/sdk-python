from enum import StrEnum


class CreateExportBodyResource(StrEnum):
    MENTIONS = "mentions"

    def __str__(self) -> str:
        return str(self.value)
