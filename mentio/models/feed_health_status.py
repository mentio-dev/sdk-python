from enum import StrEnum


class FeedHealthStatus(StrEnum):
    FAILING = "failing"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
