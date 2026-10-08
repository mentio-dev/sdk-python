from enum import StrEnum


class ExportMentionsJsonKind(StrEnum):
    COMMENT = "comment"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
