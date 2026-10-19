from enum import StrEnum


class ImportFeedsResponse200DataItemStatus(StrEnum):
    ADDED = "added"
    ALREADY = "already"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
