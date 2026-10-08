from enum import StrEnum


class ListKeywordsResponse200DataItemMatchingRepositoriesEventsItem(StrEnum):
    GROWTH = "growth"
    NEW = "new"
    STARS = "stars"
    TRACTION = "traction"

    def __str__(self) -> str:
        return str(self.value)
