from enum import StrEnum


class ExportMentionsCsvKind(StrEnum):
    COMMENT = "comment"
    POST = "post"
    REPOSITORY = "repository"

    def __str__(self) -> str:
        return str(self.value)
