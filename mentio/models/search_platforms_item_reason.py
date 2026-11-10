from enum import StrEnum


class SearchPlatformsItemReason(StrEnum):
    BUDGET = "budget"
    CREDENTIALS = "credentials"
    ERROR = "error"
    RATE_LIMITED = "rate_limited"
    TIMEOUT = "timeout"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
