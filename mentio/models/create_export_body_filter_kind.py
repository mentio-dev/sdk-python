from enum import StrEnum


class CreateExportBodyFilterKind(StrEnum):
    COMMENT = "comment"
    POST = "post"
    REPOSITORY = "repository"

    def __str__(self) -> str:
        return str(self.value)
