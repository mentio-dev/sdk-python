from enum import StrEnum


class AutomationFilterKind(StrEnum):
    COMMENT = "comment"
    POST = "post"
    REPOSITORY = "repository"

    def __str__(self) -> str:
        return str(self.value)
