from enum import StrEnum


class UsageSummaryBalanceCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
