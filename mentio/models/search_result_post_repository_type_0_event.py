from enum import StrEnum


class SearchResultPostRepositoryType0Event(StrEnum):
    GROWTH = "growth"
    NEW = "new"
    STARS = "stars"
    TOP = "top"
    TRACTION = "traction"

    def __str__(self) -> str:
        return str(self.value)
