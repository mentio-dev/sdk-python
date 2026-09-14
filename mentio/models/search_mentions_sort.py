from enum import StrEnum


class SearchMentionsSort(StrEnum):
    NEWEST = "newest"
    PRIORITY = "priority"

    def __str__(self) -> str:
        return str(self.value)
