from enum import StrEnum


class CreateExportScheduleBodyFilterKind(StrEnum):
    COMMENT = "comment"
    POST = "post"
    REPOSITORY = "repository"

    def __str__(self) -> str:
        return str(self.value)
