from enum import StrEnum


class KeywordBatchResultDataItemStatus(StrEnum):
    CREATED = "created"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
