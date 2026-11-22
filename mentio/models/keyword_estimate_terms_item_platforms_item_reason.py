from enum import StrEnum


class KeywordEstimateTermsItemPlatformsItemReason(StrEnum):
    BUDGET = "budget"
    CREDENTIALS = "credentials"
    ERROR = "error"
    PAID = "paid"
    QUOTA = "quota"
    RATE_LIMITED = "rate_limited"
    TIMEOUT = "timeout"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
