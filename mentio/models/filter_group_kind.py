from enum import StrEnum


class FilterGroupKind(StrEnum):
    COMMENT = "comment"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
