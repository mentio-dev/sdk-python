from enum import StrEnum


class ViewFilterKind(StrEnum):
    COMMENT = "comment"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
