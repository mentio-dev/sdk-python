from enum import StrEnum


class CreateViewBodyFilterKind(StrEnum):
    COMMENT = "comment"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
