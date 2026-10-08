from enum import StrEnum


class ListViewsResponse200DataItemFilterKind(StrEnum):
    COMMENT = "comment"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
