from enum import StrEnum


class WalletCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
