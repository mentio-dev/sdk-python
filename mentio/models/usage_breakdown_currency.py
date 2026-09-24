from enum import StrEnum


class UsageBreakdownCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
