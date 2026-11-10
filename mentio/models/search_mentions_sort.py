from enum import StrEnum


class SearchMentionsSort(StrEnum):
    ENGAGEMENT = "engagement"
    NEWEST = "newest"
    PRIORITY = "priority"
    REACH = "reach"

    def __str__(self) -> str:
        return str(self.value)
