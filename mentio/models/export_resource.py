from enum import StrEnum


class ExportResource(StrEnum):
    MENTIONS = "mentions"

    def __str__(self) -> str:
        return str(self.value)
