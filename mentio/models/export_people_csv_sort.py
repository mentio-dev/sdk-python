from enum import StrEnum


class ExportPeopleCsvSort(StrEnum):
    MENTIONS = "mentions"
    NEW = "new"
    REACH = "reach"
    RECENT = "recent"

    def __str__(self) -> str:
        return str(self.value)
