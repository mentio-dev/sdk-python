from enum import StrEnum


class ListFeedsResponse200DataItemHealthStatus(StrEnum):
    FAILING = "failing"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
