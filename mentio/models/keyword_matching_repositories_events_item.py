from enum import StrEnum


class KeywordMatchingRepositoriesEventsItem(StrEnum):
    GROWTH = "growth"
    NEW = "new"
    STARS = "stars"
    TRACTION = "traction"

    def __str__(self) -> str:
        return str(self.value)
