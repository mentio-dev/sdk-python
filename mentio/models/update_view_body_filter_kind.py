from enum import StrEnum


class UpdateViewBodyFilterKind(StrEnum):
    COMMENT = "comment"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
