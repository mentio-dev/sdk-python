from enum import StrEnum


class ListPeopleSort(StrEnum):
    MENTIONS = "mentions"
    NEW = "new"
    REACH = "reach"
    RECENT = "recent"

    def __str__(self) -> str:
        return str(self.value)
