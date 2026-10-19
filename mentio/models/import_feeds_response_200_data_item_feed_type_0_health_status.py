from enum import StrEnum


class ImportFeedsResponse200DataItemFeedType0HealthStatus(StrEnum):
    FAILING = "failing"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
